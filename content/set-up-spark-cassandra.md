Title: Set up Spark and Cassandra on Ubuntu 16.04
Date: 2017-05-28 17:32
Tags: spark, cassandra, ubuntu
Category: Sysadmin

The following would walk through steps to compile and set up Spark and Cassandra on a single node server on Ubuntu 16.04.

The following will be installed following the version compatibility matrix documented in [Spark Cassandra Connector](https://github.com/datastax/spark-cassandra-connector):

- Cassandra 3.0.9
- Spark 2.0.0
- Spark Cassandra Connector 2.0.1
- Scala 2.10

Start by creating a folder. This is optional but the following would assume the files are downloaded in this folder:

```commandline
sudo mkdir -p /server
sudo chown user:group /server
cd /server
```

Install __JDK 8__.

```commandline
sudo apt-get update
sudo apt-get install default-jdk
sudo add-apt-repository ppa:webupd8team/java
sudo apt-get update
sudo apt-get install oracle-java8-installer
```

Set default Java version to JDK 8 and confirm the current version.

```commandline
sudo update-alternatives --config java
java --version
```

Install __python-support__ manually as it has been removed from APT repositories for Ubuntu 16. This is required by the Cassandra Debian installer. Find the link here: https://launchpad.net/ubuntu/xenial/amd64/python-support/1.0.15.

```commandline
wget http://launchpadlibrarian.net/109052632/python-support_1.0.15_all.deb
sudo dpkg -i python-support_1.0.15_all.deb
```

Install __Cassandra__. Find the link and details here: http://docs.datastax.com/en/cassandra/3.0/cassandra/install/installDeb.html. Optionally adding =3.0.9 suffix after cassandra-tools to install this specific version as currently dsc30 installs Cassandra 3.0.9. Otherwise you may have to specify CQL protocol version later when you are running tools like __cqlsh__.

```commandline
echo "deb http://debian.datastax.com/community stable main" | sudo tee -a /etc/apt/sources.list.d/cassandra.sources.list
curl -L https://debian.datastax.com/debian/repo_key | sudo apt-key add -
sudo apt-get update
sudo apt-get install dsc30
sudo apt-get install cassandra-tools=3.0.9
```

The above would start the service automatically by naming the server "Test Cluster". If you wish to change the name of the cluster:

```commandline
sudo service cassandra stop
sudo rm -rf /var/lib/cassandra/data/system/*
```

Note with Cassandra 3.0.9 it is not as easy to modify your Cassandra cluster name in the system table and cassandra.yaml file because of [this bug](https://issues.apache.org/jira/browse/CASSANDRA-13410).

At this point you may also want to set up the Cassandra server so that the external clients and other nodes could connect to this server. Edit __/etc/cassandra/cassandra.yaml__ and update *listen_address* and *rpc_address* (or interface options) to addresses on which Cassandra would listen for connections from peer nodes and clients. Run __sudo service cassandra restart__ to restart the service.

Install __Scala__ 2.10. Find the link here: https://www.scala-lang.org/download/2.10.6.html.

```commandline
wget https://downloads.lightbend.com/scala/2.10.6/scala-2.10.6.deb
sudo dpkg -i scala-2.10.6.deb
```

The above may encounter unmet libjansi-java dependency error. Run the following to fix it.

```commandline
sudo apt-get install -f
```

Install __sbt__. Find the link here: https://bintray.com/sbt/debian/sbt/0.13.15.3#files.

```commandline
wget https://dl.bintray.com/sbt/debian/sbt-0.13.15.3.deb
sudo dpkg -i sbt-0.13.15.3.deb
```

Download source and compile __Spark__ against Scala 2.10. Find the link here: https://spark.apache.org/downloads.html. Move folder to ./spark.

```commandline
wget https://d3kbcqa49mib13.cloudfront.net/spark-2.0.0.tgz
tar -xzf spark-2.0.0.tgz
mv ./spark-2.0.0 ./spark
```

Compile Spark against Scala 2.10. See details here: https://spark.apache.org/docs/latest/building-spark.html. This may take approximately 20 minutes.

```commandline
./dev/change-scala-version.sh 2.10
./build/mvn -Pyarn -Phadoop-2.4 -Dscala-2.10 -DskipTests clean package
cp -R /server/spark/assembly/target/scala-2.10/jars /server/spark
```

Download and compile Spark Cassandra Connector. This may also take a long time.

```commandline
git clone https://github.com/datastax/spark-cassandra-connector.git
cd ./spark-cassandra-connector
git checkout tags/v2.0.1
./sbt/sbt assembly -Dscala-2.10=true
```

If you are experiencing any issue at this point, try cleaning the __Maven__ folder __rm -rf ~/.m2__ and try again.

Move the compiled connector to Spark.

```commandline
find . -iname "*.jar" -type f -exec /bin/cp {} /server/spark/jars/ \;
```

Once all the above is done, you may try starting your master, slave, and shell to test. Note you may have to change the Cassandra address to your previously set *listen_address* in *cassandra.yaml*.

```commandline
/server/spark/sbin/start-master.sh --host 0.0.0.0
/server/spark/sbin/start-slave.sh --host 0.0.0.0 spark://localhost:7077
/server/spark/bin/spark-shell --conf spark.cassandra.connection.host=127.0.0.1 --packages datastax:spark-cassandra-connector:2.0.1-s_2.10
```

You may try the [examples](https://github.com/datastax/spark-cassandra-connector/blob/master/doc/0_quick_start.md) to see if it works.

---
title: "Synopsis: Should equity factors be betting on industries?"
layout: post
date: '2021-10-11 23:43:00 +0800'
categories:
- quant
excerpt: While industry neutralization is common, certain factors carry the predictive power of industry selection, as its active factor return comes from the desirable industry exposure.
---

## Motivation

While industry neutralization is common, certain factors carry the predictive power of industry selection, as its active factor return comes from the desirable industry exposure.

## Methodology

Backtest was done with FTSE Developed Index, monthly from July 1994 to Feburary 2018. The authors crafted the following factors:

- __Within-industry factor__: <img src="https://latex.codecogs.com/svg.image?\inline&space;F_{i,t}^{within}&space;=&space;\frac{F_{i,t}&space;-&space;Median_{Industry(i)}(F_{i,t})}{k&space;\times&space;MAD_{Industry(i)FF_{i,t}}}" title="\inline F_{i,t}^{within} = \frac{F_{i,t} - Median_{Industry(i)}(F_{i,t})}{k \times MAD_{Industry(i)FF_{i,t}}}" />, where `k` = 1.4826 based on _Rousseeuw and Croux 1993_. This is industry-neutralized and therefore comparable across industries.
- __Across-industry factor__: <img src="https://latex.codecogs.com/svg.image?\inline&space;F_{i,t}^{across}&space;=&space;Median_{Industry(i)}(F_{i,t})" title="\inline F_{i,t}^{across} = Median_{Industry(i)}(F_{i,t})" />, which includes industry exposure.
- __Composite factor__: <img src="https://latex.codecogs.com/svg.image?\inline&space;F(w)&space;=&space;wF_{WI}&space;&plus;&space;(1-w)F_{AI}" title="\inline F(w) = wF_{AI} + (1-w)F_{WI}" />, where `w` controls the weight between within-industry factor and across-industry factor.

The __composite factor__ was then cross-sectionally regressed with the returns: <img src="https://latex.codecogs.com/svg.image?\inline&space;R_{i,t}&space;=&space;\alpha_{t}(w)&space;&plus;&space;\beta_{t}(w)F_{i,t}(w)&space;&plus;&space;controls_{i,t}&space;&plus;&space;\epsilon_{i,t}&space;" title="\inline R_{i,t} = \alpha_{t}(w) + \beta_{t}(w)F_{i,t}(w) + controls_{i,t} + \epsilon_{i,t} " />, where `controls` is the control variable, calculated as the average rank of factor values for the factors in the same category (i.e. value, quality, momentum, low-volatility, and size) in order to control for multicollinearity. For example, when carrying out the regression on momentum, the control variable is defined as <img src="https://latex.codecogs.com/svg.image?\inline&space;F_{i,t}^{Momentum}&space;=&space;rank[\frac{1}{3}(rank(F_{i,t}^{Mom6})&space;&plus;&space;rank(F_{i,t}^{Mom12})&space;&plus;&space;rank(F_{i,t}^{EarnRev}))]" title="\inline F_{i,t}^{Momentum} = rank[\frac{1}{3}(rank(F_{i,t}^{Mom6}) + rank(F_{i,t}^{Mom12}) + rank(F_{i,t}^{EarnRev}))]" />.

To understand the relationship between the industry exposure and factor return, observe the mean t-statistic to see if the regression is significant (> 2) for different `w` values. When it is significant as `w` is closer to 0, it would indicate a strong relationship between industry exposure and factor return. If it is significant as `w` is closer to 1, it indicates factor's own predictive power without influence of industry exposure. If it is significant across the board, then it means the factor has explanatory power by its own, and also by its industry exposure.

## Result

- Value: Overall t-statistic is increasing as `w` goes to 1, which means value factor's premium mainly comes from stock selection instead of industry selection. This is consistent across all value factors
- Quality: t-statistic decreases with `w` for ROA, ROE, and negEISS (% change in shares outstanding), which indicates less factor significance with industry neutralized, and thus quality has the power to select industry. However this is not true for other quality factors such as AssetGrowth and CFROI (Cashflow return on invested capital).
- Momentum: Short-term momentum return is mainly coming from industry exposure (e.g. MOM6), while MOM12's active return comes from both the factor itself and its industry exposure. EarnRev (earnings revisions) return is not coming from industry exposure.
- Low volatility: Industry exposure is consistently significantly contributing to the factor return regardless of volatility periods (1y, 2y, or 3y)
- Size: Defined as log of market cap, and it is also contributed by industry exposure.

## Take-away

- Perhaps inspired by Fama-French, the author cleverly constructed a `w`-bucketed regression, which gives a simple yet clear view of the influence of industry exposure for each factor, especially given the noisy nature of this analysis.
- It's worth noting from the result that MOM6 is mainly coming from industry. This probably explains why short-term momentum factor seems to be more robust in industry rotation strategies but less so on stock picking.
- Also interesting is that ROA, ROE, and negEISS has the power to select industry, but not for AssetGrowth and CFROI. A good quality strategy may combine the two flavors.
- It does match common expectations that indeed size needs to be neutralized by industry (how many of the biggest companies are tech companies?), whereas value factor is not (hence why a constant PE filter is common).

## Source

* Vyas, Krishna and Vyas, Krishna and van Baren, Michael, Should equity factors be betting on industries? (December 19, 2020). The Journal of Portfolio Management, Forthcoming, Available at SSRN: [https://ssrn.com/abstract=3423566](https://ssrn.com/abstract=3423566) or [http://dx.doi.org/10.2139/ssrn.3423566](http://dx.doi.org/10.2139/ssrn.3423566).
* URL: [https://ssrn.com/abstract=3423566](https://ssrn.com/abstract=3423566)
* DOI: [10.2139/ssrn.3423566](https://doi.org/10.2139/ssrn.3423566)

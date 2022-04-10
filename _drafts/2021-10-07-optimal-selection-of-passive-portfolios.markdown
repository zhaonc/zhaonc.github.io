---
title: "Notes: Optimal Selection of Passive Portfolios"
layout: post
date: '2021-10-07 13:58:00 +0800'
tags:
- portfolio-construction
categories:
- Notes
---
* Rudd, Andrew. “Optimal Selection of Passive Portfolios.” Financial Management 9, no. 1 (1980): 57–66. [https://doi.org/10.2307/3665314](https://doi.org/10.2307/3665314).
* URL: [https://www.jstor.org/stable/3665314](https://www.jstor.org/stable/3665314)
* DOI: [10.2307/3665314](https://doi.org/10.2307/3665314)

## Abstract

> The use of passive investment strategies, in particular index funds, has grown rapidly among institutional investors. The most frequent passive portfolio selection method is a stratification of the asset universe. This paper shows, however, that an optimization approach is a superior procedure for the efficient selection of index funds and other passive strategies.

## Notes

### Portfolio Selection By Universe Stratification

Stratifying the universe of assets. The procedures divides the universe into "cells", and then selects assets from the cells. The heuristic selects first by matching the fund and the index by company size and then by one other dimension (e.g. industry groups).

> 1. Assemble the universe of assets
> 2. Specify the dollar value of the index fund
> 3. Select the minimum investment size
> 4. Form a cap-weighted portfolio with total value from all assets in the universe, and rank holdings from largest to smallest. Purchase assets that have holdings greater than minimum position size.
> 5. Assign each asset in the universe to one of N mutually exclusive and exhaustive cells.
> 6. Rank the cells in order of the difference between the fund and index holdings, from the most to the least deficient. Starting with the most deficient cell, and with assets in that cell that have not yet been purchased in step 4, purchase single units until the index fund cell holding matches the index cell holding to a dicrepancy of one unit or less.

The intuition that keeping the differences in holdings small will cause the tracking error to be small is erroneous: "The reason is that residual risk is composed of two components, specific risk and extra-market covariance (XMC)"

> * By starting with the larger capitalization stocks, the index fund may well be underweighted with small stocks.
> * the procedure does not control the risk level of the index fund.
> * there is no indication of the relative benefit or cost of adding or deleting a stock.

### The Optimization Approach

> The optimization approach results in a quadratic program, since residual risk is inescapably a quadratic function of the asset holdings. The control of systematic risk is effected as a single linear constraint requiring the portfolio beta to be unity, while the control of residual risk is implemented directly from a model of the residual covariance among assets.

Incorporating transaction costs: "The only trades undertaken are where the benefit is greater than the cost."

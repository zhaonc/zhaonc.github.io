---
title: "Notes: Should equity factors be betting on industries?"
layout: post
date: '2021-10-11 23:43:00 +0800'
tags:
- factor-investing
categories:
- Notes
---
* Vyas, Krishna and Vyas, Krishna and van Baren, Michael, Should equity factors be betting on industries? (December 19, 2020). The Journal of Portfolio Management, Forthcoming, Available at SSRN: [https://ssrn.com/abstract=3423566](https://ssrn.com/abstract=3423566) or [http://dx.doi.org/10.2139/ssrn.3423566](http://dx.doi.org/10.2139/ssrn.3423566).
* URL: [https://ssrn.com/abstract=3423566](https://ssrn.com/abstract=3423566)
* DOI: [10.2139/ssrn.3423566](https://doi.org/10.2139/ssrn.3423566)

## Abstract

> Asset managers are increasingly incorporating equity factors that deviate from traditional academic definitions in their stock selection process. We show that these factors frequently exhibit strong industry biases, making it crucial to understand the interaction between factor exposure and traditional industry exposure. Industry exposure plays a major role in the risk profile of a portfolio, making unintended industry exposures costly. For an extensive set of 21 equity factors, beyond the standard academic factors, we examine which equity factors are rewarded for their industry allocation. This set spans the value, quality, momentum, low volatility, and size investment styles. We use a global and liquid investment universe, as is commonly used by large institutional asset managers. We find that equity factors from the same investment style, most notably momentum and quality, exhibit strong differences in their returns from industry allocation. Understanding the interaction between factors and industry exposures can lead to higher return premiums, and lower portfolio volatility without harming performance.

## Notes

### Rationale

While industry neutralization is common, certain factors carry the predictive power of industry selection, as its active factor return comes from the desirable industry exposure.

### Experiment

__Data__: FTSE Developed Index, monthly from July 1994 to Feburary 2018.

__Methodology__:

- __Within-industry factor__: <img src="https://latex.codecogs.com/svg.image?\inline&space;F_{i,t}^{within}&space;=&space;\frac{F_{i,t}&space;-&space;Median_{Industry(i)}(F_{i,t})}{k&space;\times&space;MAD_{Industry(i)FF_{i,t}}}" title="\inline F_{i,t}^{within} = \frac{F_{i,t} - Median_{Industry(i)}(F_{i,t})}{k \times MAD_{Industry(i)FF_{i,t}}}" />, where `k` = 1.4826 based on _Rousseeuw and Croux 1993_. This is industry-neutralized and therefore comparable across industries.
- __Across-industry factor__: <img src="https://latex.codecogs.com/svg.image?\inline&space;F_{i,t}^{across}&space;=&space;Median_{Industry(i)}(F_{i,t})" title="\inline F_{i,t}^{across} = Median_{Industry(i)}(F_{i,t})" />, which includes industry exposure.
- __Composite factor__: <img src="https://latex.codecogs.com/svg.image?\inline&space;F(w)&space;=&space;wF_{WI}&space;&plus;&space;(1-w)F_{AI}" title="\inline F(w) = wF_{AI} + (1-w)F_{WI}" />, where `w` controls the weight between within-industry factor and across-industry factor.
- Cross-sectionally regress the __composite factor__ with return: <img src="https://latex.codecogs.com/svg.image?\inline&space;R_{i,t}&space;=&space;\alpha_{t}(w)&space;&plus;&space;\beta_{t}(w)F_{i,t}(w)&space;&plus;&space;controls_{i,t}&space;&plus;&space;\epsilon_{i,t}&space;" title="\inline R_{i,t} = \alpha_{t}(w) + \beta_{t}(w)F_{i,t}(w) + controls_{i,t} + \epsilon_{i,t} " />, where `controls` is the control variable, calculated as the average rank of factor values for the factors in the same category (i.e. value, quality, momentum, low-volatility, and size) in order to control for multicollinearity. For example, when carrying out the regression on momentum, the control variable is defined as <img src="https://latex.codecogs.com/svg.image?\inline&space;F_{i,t}^{Momentum}&space;=&space;rank[\frac{1}{3}(rank(F_{i,t}^{Mom6})&space;&plus;&space;rank(F_{i,t}^{Mom12})&space;&plus;&space;rank(F_{i,t}^{EarnRev}))]" title="\inline F_{i,t}^{Momentum} = rank[\frac{1}{3}(rank(F_{i,t}^{Mom6}) + rank(F_{i,t}^{Mom12}) + rank(F_{i,t}^{EarnRev}))]" />. Observe the mean t-statistic to see if the regression is significant (> 2) for different `w` values. When it is significant as `w` is closer to 0, it would indicate a strong relationship between industry exposure and factor return. If it is significant as `w` is closer to 1, it indicates factor's own predictive power without influence of industry exposure. If it is significant across the board, then it means the factor has explanatory power by its own, and also by its industry exposure.

__Result__:

- Value: Overall t-statistic is increasing as `w` goes to 1, which means value factor's premium mainly comes from stock selection instead of industry selection. This is consistent across all value factors
- Quality: t-statistic decreases with `w` for ROA, ROE, and negEISS (% change in shares outstanding), which indicates less factor significance with industry neutralized, and thus quality has the power to select industry. However this is not true for other quality factors such as AssetGrowth and CFROI (Cashflow return on invested capital).
- Momentum: Short-term momentum return is mainly coming from industry exposure (e.g. MOM6), while MOM12's active return comes from both the factor itself and its industry exposure. EarnRev (earnings revisions) return is not coming from industry exposure.
- Low volatility: Industry exposure is consistently significantly contributing to the factor return regardless of volatility periods (1y, 2y, or 3y)
- Size: Defined as log of market cap, and it is also contributed by industry exposure.

__Conclusion__: Most factors have tendency for industry exposure, and therefore would benefit from neutralization. Factors may have inconsistent behavior even within the same category, and therefore neutralization should be applied with care.

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Metis Pre-work: Statistics

@author: Sakina Zabuawala
"""
import numpy as np
import scipy.stats
import random

import thinkstats2
import thinkplot

import nsfg
import first
from estimation import RMSE, MeanError
import hinc
import hinc2
import hypothesis

def BiasPmf(pmf, label):
    new_pmf = pmf.Copy(label=label)
    for val, prob in new_pmf.Items():
        new_pmf[val] *= val
    new_pmf.Normalize()
    return new_pmf

preg = nsfg.ReadFemPreg()
resp = nsfg.ReadFemResp()

live, firsts, others = first.MakeFrames()

#--- Chapter2 Ex4
wgt_live = live.totalwgt_lb.dropna()
wgt_first = firsts.totalwgt_lb.dropna()
wgt_other = others.totalwgt_lb.dropna()
mean_diff = 100*(wgt_first.mean()-wgt_other.mean())/wgt_live.mean()
wgt_cohend = thinkstats2.CohenEffectSize(wgt_first, wgt_other)
plen_cohend = thinkstats2.CohenEffectSize(firsts.prglngth, others.prglngth)
print('Difference in relative mean:', mean_diff)
print('Cohen\'s d for total weight in lbs:', wgt_cohend)
print('Cohen\'s d for pregnancy length in weeks:', plen_cohend)

#--- Chapter3 Ex1
actual_pmf = thinkstats2.Pmf(resp.numkdhh, label='actual')
biased_pmf = BiasPmf(actual_pmf, label='biased')
thinkplot.PrePlot(2)
actual_hist = thinkplot.Pmf(actual_pmf)
biased_hist = thinkplot.Pmf(biased_pmf)
thinkplot.Show(xlabel='#kids in household', ylabel='PMF')
print('Actual Mean:', actual_pmf.Mean())
print('Biased Mean:', biased_pmf.Mean())
              
#--- Chapter4 Ex2
my_seq = np.random.random(1000)
my_pmf = thinkstats2.Pmf(my_seq)
my_cdf = thinkstats2.Cdf(my_seq)
thinkplot.Pmf(my_pmf, linewidth=0.1)
thinkplot.Show(xlabel='Random variable', ylabel='PMF')
thinkplot.Cdf(my_cdf)
thinkplot.Show(xlabel='Random variable', ylabel='CDF')

#--- Chapter5 Ex1
mu = 178
sigma = 7.7
mhgt_dist = scipy.stats.norm(loc=mu, scale=sigma)
m1 = 177.8 #5'10" in cm
m2 = 185.42 #6'1" in cm
print('Percent Male population between 5\'10" and 6\'1" is %.2f' 
      %(100*(mhgt_dist.cdf(m2)-mhgt_dist.cdf(m1))))

#--- Chapter7 Ex1
live_ss = live.dropna(subset=['agepreg', 'totalwgt_lb'])
thinkplot.Scatter(live_ss.agepreg, live_ss.totalwgt_lb, 
                  alpha=0.05, s=10)
thinkplot.Config(xlabel='Mother age (years)',
                 ylabel='Birth weight (lbs)',
                 legend=False)

bins = np.arange(15,42,3)
indices = np.digitize(live_ss.agepreg, bins)
groups = live_ss.groupby(indices)

age_means = [g.agepreg.mean() for i,g in groups]
wgt_cdfs = [thinkstats2.Cdf(g.totalwgt_lb) for i,g in groups]

percentiles = [75, 50, 25]
thinkplot.PrePlot(len(percentiles))
for percent in percentiles:
    wgt_percentile = [cdf.Percentile(percent) for cdf in wgt_cdfs]
    label = '%dth' %percent
    thinkplot.Plot(age_means, wgt_percentile, label=label)
thinkplot.Config(xlabel='Mother age (years)',
                 ylabel='Birth weight (lbs)',
                 legend=True)

p_corr = thinkstats2.Corr(live_ss.agepreg, live_ss.totalwgt_lb)
s_corr = thinkstats2.SpearmanCorr(live_ss.agepreg, live_ss.totalwgt_lb)
print('Pearson\'s Correlation:', p_corr)
print('Spearman\'s Correlation:', s_corr)

#--- Chapter8 Ex2
def SimulateSample(lam=2, n=10, iters=1000):
    lams_est = []
    for m in np.arange(iters):
        xs = np.random.exponential(1.0/lam, n)
        L = 1/np.mean(xs)
        lams_est.append(L)    
    return lams_est

def SampleDistrPLot(estimates, n, lam):
    label = 'n=%d' %n
    cdf = thinkstats2.Cdf(estimates, label=label)
    conf_int = cdf.Percentile(5), cdf.Percentile(95)
    stderr = RMSE(estimates, lam)
    print('n=', n, 'Std Error=', stderr, 'Conf Int=', conf_int)
    thinkplot.Cdf(cdf)
    thinkplot.Plot([conf_int[0], conf_int[0]], [0,1], color='0.8', linewidth=2)
    thinkplot.Plot([conf_int[1], conf_int[1]], [0,1], color='0.8', linewidth=2)

n_arr = [10, 50, 100, 1000]
lam = 2

thinkplot.PrePlot(len(n_arr))
for n in n_arr:
    lams = SimulateSample(lam, n, 1000)   
    SampleDistrPLot(lams, n, lam)
    
thinkplot.Config(xlabel='L estimate',
                 ylabel='CDF',
                 title='Sampling distribution',
                 xlim=[0,4],
                 legend=True)      
  
#--- Chapter6 Ex1
df = hinc.ReadData()
log_sample = hinc2.InterpolateSample(df, log_upper=6.0)
sample = np.power(10, log_sample)
print('Mean = ', sample.mean())
print('Median =', thinkstats2.Median(sample))
print('Skewness =', thinkstats2.Skewness(sample))
print('Pearson Median Skweness =', thinkstats2.PearsonMedianSkewness(sample))
income_cdf = thinkstats2.Cdf(sample)
print(income_cdf.Prob(sample.mean())*100)  

#--- Chapter8 Ex3
def SimulateGame(lam):
    t = 0
    goals = 0
    while True:
        time_int = random.expovariate(lam)
        t += time_int
        if t>1:
            break
        goals += 1
    return goals

def SimulateManyGames(lam, iters=1000000):
    lam_est = []
    for _ in np.arange(iters):
        lam_est.append(SimulateGame(lam))
    print('Mean Error =', MeanError(lam_est, lam))
    print('RMSE =', RMSE(lam_est, lam))
    lam_cdf = thinkstats2.Cdf(lam_est)
    ci = lam_cdf.Percentile(5), lam_cdf.Percentile(95)
    lam_pmf = thinkstats2.Pmf(lam_est)
    thinkplot.Cdf(lam_cdf)
    thinkplot.Plot([ci[0], ci[0]], [0,1], linewidth=2, color='0.8')
    thinkplot.Plot([ci[1], ci[1]], [0,1], linewidth=2, color='0.8')
    thinkplot.Config(xlabel='Goals per game',
                     ylabel='CDF',
                     legend=False)

SimulateManyGames(2)
SimulateManyGames(4)

#--- Chapter9 Ex1
def RunTests(df, iters=1000):
    n = len(df)
    
    firsts_n = df[df.birthord==1]
    others_n = df[df.birthord!=1]
    
    data = firsts_n.prglngth.values, others_n.prglngth.values
    ht = hypothesis.DiffMeansPermute(data)
    p1 = ht.PValue(iters=iters)
    
    data = firsts_n.prglngth.values, others_n.prglngth.values
    ht = hypothesis.DiffMeansOneSided(data)
    p2 = ht.PValue(iters=iters)
    
    data = firsts_n.totalwgt_lb.values, others_n.totalwgt_lb.values
    ht = hypothesis.DiffMeansPermute(data)
    p3 = ht.PValue(iters=iters)
    
    data = df.agepreg.values, df.totalwgt_lb.values
    ht = hypothesis.CorrelationPermute(data)
    p4 = ht.PValue(iters=iters)

    data = firsts_n.prglngth.values, others_n.prglngth.values
    ht = hypothesis.PregLengthTest(data)
    p5 = ht.PValue(iters=iters)

    data = firsts_n.totalwgt_lb.values, others_n.totalwgt_lb.values
    ht = hypothesis.PregLengthTest(data)
    p6 = ht.PValue(iters=iters)

    print('%d\t%.2f\t%.2f\t%.2f\t%.2f\t%.2f\t%.2f\n' %(n, p1, p2, p3, p4, p5, p6))

live, firsts, others = first.MakeFrames()   

n = len(live)
for _ in range(8):
    live_n = thinkstats2.SampleRows(live, n)
    RunTests(live_n, 5000)
    n //= 2
    
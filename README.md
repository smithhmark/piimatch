# piimatch
Fuzzy Matching for PII

# Goals
Matching identies is tricky, for example multiple spellings and differing collections of PII in different mentions. The goal of this library is to provide options for comparing identites.

# Plan

1. focus on pure python 3.x
   1. Start with a relatively simple full name matcher
   1. provide an ID matcher (for things like govt ids)
   1. explore ways to compine feature scores into identity scores
   1. North American address matching
1. Native C code support? 

# Getting started
```
$ pipenv install --all
```

running tests:
`$ pipenv run tests`

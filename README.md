#Finding common, reputable sources of economic analysis

These scripts look for the most common web domains recommended
in daily links by two popular economic blogs:
Tyler Cowen's Marginal Revolution and Mark Thoma's Economist's View

##Overview

The scripts require a Bing web search API key.
API.py contains a function for accessing the API.

The scripts should be run in the following order:
    1. get_recs.py
    2. rec_cleanup.py
    3/4. MR_parser.py
    3/4. EV_parser.py
    5. analysis.py

The files Recs_from_EV and Recs_from_MR contain URLs recommended by the two sites.

Analysis.py outputs common domains. For more, see my blog:

http://www.beyondthetimes.com/?p=1815
    

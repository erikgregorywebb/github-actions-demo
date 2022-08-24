## Github Actions Demo

Web scraping is a useful tool for data practitioners, to state the obvious. Often, scraping is most valuable when performed on a scheduled basis, to incorporate new or refreshed values into the dataset.

In the past, I’ve paid a (small) monthly fee to [PythonAnywhere](https://www.pythonanywhere.com/) to run scraping jobs. However, there’s a better, free alternative offered by a familiar platform: [GitHub Actions](https://docs.github.com/en/actions). While GitHub Actions is largely designed for code deployment automation (testing pull requests, deploying merged pull requests to production) it can also be used to run jobs, including web scraping jobs.

This [blog post](https://unboxed-analytics.com/data-technology/github-actions-for-data-analysts/) walks through the implementation of a simple GitHub action, which scrapes the headline mortgage rates posted on Freddie Mac’s [home page](http://www.freddiemac.com/) daily.

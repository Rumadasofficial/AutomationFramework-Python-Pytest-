#! /usr/bin/env sh
pytest -v -s -m "sanity" --html=Reports/report.html testCases/ --browser chrome
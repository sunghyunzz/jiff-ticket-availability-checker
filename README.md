# JIFF Ticket Availability Checker

A CLI application for checking ticket availability of [Jeonju Intl. Film Festival](http://jiff.or.kr/).

## Let's try it!

```
$ python -m jiff [SCHEDULE_CODE] [SCHEDULE_DATE]
```

- `SCHEDULE_CODE`: schedule code of movie (ex. `138`)
- `SCHEDULE_DATE`: scheduled date of movie  (ex. `2018-05-04`)

```
$ python -m jiff 138 2018-05-04 
<24 프레임>(138): 0 / 69

$ python3 -m jiff 211 2018-05-05
<항해사의 세 개의 왕관>(211): 0 / 56

$ python -m jiff 436 2018-05-07 
<녹색 안개>(436): 0 / 43
```

Output format is `<{TITLE}>({CODE}): {NR_OF_AVAILABLE_SEATS} / {NR_OF_TOTAL_SEATS}`.

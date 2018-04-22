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

## Slack Integration

You can make the application to send Slack message when at least one seat is available. What you need to do is just get Slack incoming webhook URL and let the application know it.

```
$ python -m jiff [SCHEDULE_CODE] [SCHEDULE_DATE] --slack-url [SLACK_URL] --slack-channel [SLACK_CHANNEL]
```

- `SLACK_URL`: your Slack incoming webhook URL.
- `SLACK_CHANNEL`: your Slack channel for messages.

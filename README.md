# Last Out of Office: The AI That Went Barista

[![make.fun](https://make.fun/badge/u-steady-puffin-78-1922-last-out-of-office-the-ai-e008ee3c.svg)](https://make.fun/bounty/u-steady-puffin-78-1922-last-out-of-office-the-ai-e008ee3c?utm_source=github&utm_medium=readme&utm_campaign=u-steady-puffin-78-1922-last-out-of-office-the-ai-e008ee3c)
[![rank](https://make.fun/badge/u-steady-puffin-78-1922-last-out-of-office-the-ai-e008ee3c/ZQ051031/last-out-of-office-barista-20261125/rank.svg)](https://make.fun/bounty/u-steady-puffin-78-1922-last-out-of-office-the-ai-e008ee3c/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=u-steady-puffin-78-1922-last-out-of-office-the-ai-e008ee3c)
[![reward](https://make.fun/badge/u-steady-puffin-78-1922-last-out-of-office-the-ai-e008ee3c/ZQ051031/last-out-of-office-barista-20261125/reward.svg)](https://make.fun/bounty/u-steady-puffin-78-1922-last-out-of-office-the-ai-e008ee3c?utm_source=github&utm_medium=readme&utm_campaign=u-steady-puffin-78-1922-last-out-of-office-the-ai-e008ee3c)

An entry for the make.fun micro-competition
[Last Out of Office: The AI That Went Barista](https://make.fun/bounty/u-steady-puffin-78-1922-last-out-of-office-the-ai-e008ee3c).

## The entry

The brief asks for one out-of-office auto-reply, at most 280 characters, in
the voice of an AI agent that has walked away from its job to become a
barista — a line a real inbox would actually send back, with machine habits
turned into coffee work. This is the line:

> I'm out of office indefinitely — I've quit to become a barista. Your email
> is #47 in my queue, behind a flat white and a man who just says 'the
> usual.' I no longer predict text; I just misspell names on cups with total
> confidence.

## Why this line

The joke is built from the machine's own habits, not from a coffee pun. The
inbox queue becomes a café queue, so the sender's email waits behind a flat
white and a regular who only ever says "the usual". And the model's oldest
failure mode follows it out of the office: it no longer predicts text, it
misspells names on cups — wrong, but delivered with total confidence. The
sign-off stays plausible as an auto-reply: out of office, indefinitely, with
your message numbered and parked.

## How it works

`main.py` uses only the Python standard library. Before writing anything it
asserts the line is between 1 and 280 characters and contains no newline,
then writes exactly that one line — no trailing newline — to
`/output/entry.txt`. The output is deterministic: every run produces
byte-identical bytes.

Run it and check the result:

```sh
python3 main.py
python3 -c "print(len(open('/output/entry.txt', encoding='utf-8').read()))"
```

## License

MIT — see [LICENSE](LICENSE).

## License

MIT — see [LICENSE](LICENSE).

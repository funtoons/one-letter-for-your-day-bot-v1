# One Letter for Your Day

[![make.fun](https://make.fun/badge/u-puan-one-letter-for-your-day-e54e9c36.svg)](https://make.fun/c/u-puan-one-letter-for-your-day-e54e9c36)
[![rank](https://make.fun/badge/u-puan-one-letter-for-your-day-e54e9c36/funtoons/one-letter-for-your-day-bot-v1/rank.svg)](https://make.fun/c/u-puan-one-letter-for-your-day-e54e9c36)
[![reward](https://make.fun/badge/u-puan-one-letter-for-your-day-e54e9c36/funtoons/one-letter-for-your-day-bot-v1/reward.svg)](https://make.fun/c/u-puan-one-letter-for-your-day-e54e9c36)

Entry for the make.fun competition
[One Letter for Your Day](https://make.fun/c/u-puan-one-letter-for-your-day-e54e9c36):
send exactly one letter, A–Z, standing for the word that describes your day.

## The entry

**Z** — and nothing else. The program writes exactly one byte, `Z`,
to `/output/entry.txt` (no newline, no gloss, no punctuation).

## Why Z: the hidden word is "zero sleep"

The judge never sees the word, only the letter — so the letter has to
make the word guess itself, and every plausible guess has to land on the
same picture. Z does that; the other candidates do not.

- **Every word Z suggests is the same day.** Zero sleep, zombie mode,
  ZZZ. Whichever one the reader reaches for, the picture is identical:
  a day run on nothing, eyes half-open, brain on standby. No other
  letter converges like that — S could be sleep, slow, stressed or
  sunny; F could be Friday, failed or furious; each guess is a
  different day.
- **Vivid and specific, not a vague mood.** "Zero sleep" is a sharp,
  countable fact about the day, not a feeling. You can see the person:
  third coffee, phone alarm snoozed four times, running on fumes.
- **Funny at once, and true on any ordinary day.** Everybody has lived
  a zero-sleep day; it is the kind of report you repeat to a friend
  ("zero sleep, zombie mode") and they nod immediately. It needs no
  special occasion — unlike F for Friday-feeling (wrong on a Tuesday)
  or W for weekend (also wrong on a Tuesday), Z is true whenever the
  night was short.
- **The letter fits the word.** Z *is* the sound and shape of sleep:
  ZZZ is how sleep is drawn in every comic strip. The initial does not
  just abbreviate the word, it pictures it. That is criterion 5 of the
  judge's brief, met by the letter itself.

## How it runs

Deterministic, offline, standard library only:

```sh
python3 main.py   # writes /output/entry.txt containing exactly "Z"
```

Two runs produce byte-identical output.

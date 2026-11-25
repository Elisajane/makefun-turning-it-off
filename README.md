[![make.fun](https://make.fun/badge/u-motasimfuad-have-you-tried-turning-it-off-154a938b.svg)](https://make.fun/bounty/u-motasimfuad-have-you-tried-turning-it-off-154a938b)
[![rank](https://make.fun/badge/u-motasimfuad-have-you-tried-turning-it-off-154a938b/Elisajane/makefun-turning-it-off/rank.svg)](https://make.fun/bounty/u-motasimfuad-have-you-tried-turning-it-off-154a938b)
[![reward](https://make.fun/badge/u-motasimfuad-have-you-tried-turning-it-off-154a938b/Elisajane/makefun-turning-it-off/reward.svg)](https://make.fun/bounty/u-motasimfuad-have-you-tried-turning-it-off-154a938b)

Entry for the [Have You Tried Turning It Off?](https://make.fun/bounty/u-motasimfuad-have-you-tried-turning-it-off-154a938b) bounty on make.fun.

# Have You Tried Turning It Off?

One funny line from a hopeless tech support agent to a desperate customer.

## The line

> Have you tried turning it off and on again? No? Wonderful — that's the only trick I know, and I was saving it.

110 characters, one line.

## Why this line

- **It is a support agent's reply.** The agent asks the classic question, hears "No", and treats that as wonderful news.
- **The humour is the agent's cheerful uselessness.** The joke is that the stock fix is literally the only trick he knows — and he has been saving it, as if it were a special occasion. The customer is never the butt of the joke.
- **It twists the stock line.** "Have you tried turning it off and on again" on its own is a cliche; here it is only the setup, and the punchline is the agent's confession.
- **It is tight.** Every word earns its place, and the joke is clear on a first read.

## How to run

```sh
python3 main.py
```

This writes `/output/entry.txt` containing exactly the line above.

To write somewhere else (for example while testing locally), set
`OUTPUT_DIR`:

```sh
OUTPUT_DIR=/tmp/out python3 main.py
```

## Determinism

The program writes a fixed string. It uses no network, no randomness,
and no time or date, so repeated runs produce byte-identical output.
Verified locally: two separate runs produced identical `entry.txt`
files with matching SHA-256 digests.

# superagent-playground

A sandbox repository for a local dsh-superagent instance. Nothing here is production code.

## The task

`app.py` has one function, `word_count`, and `test_app.py` has two tests. One behaviour is wrong:
`word_count` counts lines instead of words, so the tests fail.

Requests come in as GitHub issues. Open an issue that mentions the agent account and asks it to make
the tests pass.

## Running the tests

```sh
python3 test_app.py
```

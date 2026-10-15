# Tests

Run tests from the repository root:

```bash
pip install -r requirements.txt
python -m unittest discover -s app/tests -v
```

These are basic smoke tests for the educational API. Expand tests for issue/return, overdue fine calculations, invalid identifiers, authorization, and concurrent operations before using the system beyond a demo.

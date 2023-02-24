# Getting Captain working with unittest

## 1. 🧪 Ensure unittest produces junit output

`unittest` doesn't natively support writing output to a file, but you can use `unittest-xml-reporting` as your test runner to produce junit output without having to modify your tests at all.

```sh
pip install unittest-xml-reporting
python -m xmlrunner -o tmp
```

will produce Captain-compatible xml output in the `tmp/` directory.

## 2. 🔐 Create an Access Token

Create an Access Token for your organization within [Captain][captain] ([more documentation here][create-access-token]).

Add the new token as an action secret to your repository. Conventionally, we call this secret `RWX_ACCESS_TOKEN`.

## 3. 💌 Install the Captain CLI and call it when running tests

See the [full documentation on test suite integration][test-suite-integration]. Use a glob when specifying `--test-results` since `unittest-xml-reporting` will write multiple files by default. You'll also need to specify `--language Python` and `--framework unittest` to inform the Captain CLI about how to interpret the test result files.

```yaml
- uses: rwx-research/setup-captain@v1
- name: Run tests
  run: |
    captain run \
      --suite-id captain-examples-unittest \
      --test-results tmp/*.xml \
      --language Python \
      --framework unittest \
      -- python -m xmlrunner -o tmp
  env:
    RWX_ACCESS_TOKEN: ${{ secrets.RWX_ACCESS_TOKEN }}
```

## 4. 🎉 See your test results in Captain!

Take a look at the [final workflow!][workflow-with-captain]

[workflow-before-captain]: https://github.com/captain-examples/unittest/blob/basic-workflow/.github/workflows/ci.yml
[captain]: https://account.rwx.com/deep_link/manage/access_tokens
[create-access-token]: https://www.rwx.com/docs/access-tokens
[workflow-with-captain]: https://github.com/captain-examples/unittest/blob/main/.github/workflows/ci.yml
[test-suite-integration]: https://www.rwx.com/captain/docs/test-suite-integration

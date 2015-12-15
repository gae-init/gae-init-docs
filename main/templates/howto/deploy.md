Make sure that you have created a new application on
[App Engine](https://console.developers.google.com/project)
and the name of the application is updated in the
[`app.yaml`](https://github.com/gae-init/gae-init/blob/master/main/app.yaml#L1).

To deploy your application execute the following command from the root directory:

```bash
$ gulp deploy
```

If you wish to deploy it to a different application or a version then execute:

```bash
$ gulp deploy --application=foo --version=bar
```

To deploy your app to App Engine, you will need to register a project to create your project ID, which will determine the URL for the app.

1. In the Cloud Platform Console, go to the [Projects page](https://console.cloud.google.com/project) and select or create a new project.
2. Note the project ID that you created above.
3. Upload your application to Google App Engine by invoking the following command from the root directory. This opens a browser window for you to sign in using your Google account. You'll be providing the project ID as the argument for `--project`.

    ```
    gulp deploy --project=<YOUR_PROJECT_ID>
    ```

4. Your app is now deployed and ready to serve traffic at `https://<YOUR_PROJECT_ID_>.appspot.com/`

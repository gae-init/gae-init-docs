Deploy your app to Google App Engine, so that anyone can access your app in the cloud. You will need to register a project (or re-use an existing one) and obtain the Project ID, as this will determine the web address for the app.

1. In the Cloud Platform Console, go to the [Projects page](https://console.cloud.google.com/project) and select or create a new project.

2. Note the Project ID of that project.

3. Deploy your application to Google App Engine, using the above Project ID as an argument:

    ```
    gulp deploy --project=<YOUR_PROJECT_ID>
    ```

4. When finished, your app will be ready to serve traffic at `https://<YOUR_PROJECT_ID>.appspot.com/`

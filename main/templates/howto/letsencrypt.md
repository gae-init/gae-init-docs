Use the [Google Cloud Shell](https://cloud.google.com/cloud-shell/docs/) to
execute the following docker commands:

```bash
docker run -it -p 443:443 -p 80:80 \
  -v "$(pwd)/ssl-keys:/etc/letsencrypt" \
  quay.io/letsencrypt/letsencrypt:latest \
  -a manual certonly
```

After following the instructions and filling the URL and email for the custom
domain, you should be able to get the **challenge** and the **response** back.
Copy/paste them into the **Admin > SSL** to the respected fields on the
deployed version of the app.

As a final step we need to upload the certificiats to App Engine, but before
that convert private key to a compatible format (replace `www.example.com` with
your actual domain):

```bash
openssl rsa -inform pem \
  -in live/www.example.com/privkey.pem \
  -outform pem > live/www.example.com/privkey_fixed.pem
```

After uploading the `live/www.example.com/cert.pem` and
`live/www.example.com/privkey_fixed.pem` to the App Engine settings for
[SSL Certificats](https://console.developers.google.com/appengine/settings/certificates)
and setting up the custom domain everything should work.

> For more details and screenshots follow the [instructions by Igor
Artamonov](http://igorartamonov.com/2015/12/lets-encrypt-ssl-google-appengine/).

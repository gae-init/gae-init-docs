If the `&next` argument is provided in the URL then this function will return its value.

If the `&next` argument is not present then it will return the `referrer` URL, but only if it's from the same domain. Very useful when you want to return to the same page that you've been before, after completing a certain action, like sign in page or edit of the form.

When nothing is present it will simply return the URL of the welcome page.

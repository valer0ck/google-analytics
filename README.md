# Google-analytics
Show google analytics for your website without google login form. It was developed for Python/Django. I tested it with 1.9 version but lib provided by google is able for lowest versions

### Introduction
Google provide libraries for languages like Python, PHP and others to implementing google analitycs and other google APIs into your website without login form, it uses a token for authorization when accesing a Google API service. For Javascript its also provided a library, but for security reasons you must access trought google login form.

For authentication and authorization google uses Oauth 2.0 protocol.

I did this app at [Elemental Lab](http://elementalab.com) because we are building a Content Management System (CMS) and we needed to show statistics to clients.

### Usage
  - Clone repository
  - Install requirements
  - Configure settings (explained below)
  - Runserver

### Configure settings

For testing this app only its needed to modify settings file.

Go to [Google analytics](http://www.google.com/analytics/), create a property and add to all pages of your website the tracking code provided (I suppose you already know about it). Code its something like this:
```sh
  <script>
    (function(i,s,o,g,r,a,m){i['GoogleAnalyticsObject']=r;i[r]=i[r]||function(){
    (i[r].q=i[r].q||[]).push(arguments)},i[r].l=1*new Date();a=s.createElement(o),
    m=s.getElementsByTagName(o)[0];a.async=1;a.src=g;m.parentNode.insertBefore(a,m)
    })(window,document,'script','https://www.google-analytics.com/analytics.js','ga');

    ga('create', 'UA-XXXXXXXX-X', 'auto');
    ga('send', 'pageview');
  </script>
```

###### Lets get the data for empty Constants
settings.py got this segment of code at the end:

```sh
# Google APIs
SCOPE = ['https://www.googleapis.com/auth/analytics.readonly']
# Service Account.
SERVICE_ACCOUNT_EMAIL = ''
# Path to the Service Account's Private Key file.
SERVICE_ACCOUNT_JSON_FILE_PATH = os.path.join(
    BASE_DIR,
    '',
)

VIEW_ID = ''
```

I already added google analytics to **SCOPE**, [here](https://developers.google.com/identity/protocols/googlescopes) you can find all OAuth 2.0 scopes

#### Google Developers Console

Next, go to [Google Developers Console] (https://console.developers.google.com) and create a new project (I use one single project for managing several websites), then go to **Overview** and look for APIs you need to enable (I enabled Analytics API). Remember to add enabled APIs to **SCOPE**

Go to credentials, here you can create credentials for enabled APIs, select **Create credential** and **Key Service Account**, then select your account service and JSON key type, next, click on create. It will download a JSON file, save it at / of project

```sh
google-analytics
   google_analytics
   public
   templates
   ...
   name_of_file.json
   ...
```

And copy the name of the file and paste in this way:

```sh
SERVICE_ACCOUNT_JSON_FILE_PATH = os.path.join(
    BASE_DIR,
    'name_of_file.json',
)
```

Go to main menu an select **IAM**, here you will add service accounts for you created in Google Developers Console. Click in **Service Account** and **Create Service Account**. Add a name to the account, it will generate an **Account Service Id**, finally click on **create**.

Copy the Account Service Id and paste in SERVICE_ACCOUNT_EMAIL within single quotes.

#### Google Analytics Account

Into your google analytics account select a domain and go to **Admin**, then go to **VIEW** in section **View Settings**.

There it is your **VIEW ID**, just copy and paste in **VIEW_ID** within single quotes

Finally you need to give permissions to your Service Account Id created in Google Developers Console. Go to **Users Management** and add permissions to the account.

Google analitycs allow users view or analyze statistics, here you can't read, analyze, edit or manage users, so i only provide permissions for read and analyze. Be careful with this topic, for security add the necesary permissions.

#### Code

Previous method for getting credentials was SignedJwtAssertionCredentials (imported from oauth2client.client), right now its used ServiceAccountCredentials (imported from oauth2client.service_account). Oauth2client Changelog suggest JSON keys rather than .p12 keys. [Changelog](https://github.com/google/oauth2client/blob/master/CHANGELOG.md#special-note-about-serviceaccountcredentials)


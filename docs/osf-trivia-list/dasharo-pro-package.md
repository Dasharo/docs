# Frequently Asked Questions about Dasharo Pro Package

## How can I download the Dasharo Pro Package binaries?

If you've purchased the Dasharo Pro Package, you should have received an
email containing all the necessary details to access your binaries. Here's how
you can download them:

1. **Locate Your Email:** Check the email account you used to purchase the
   subscription. Look for an email from Dasharo that includes your subscription
   data. This email will contain several vital pieces of information:

    - **Logs Key:** A key you might need for other operations or support.
    - **Download Key:** A unique string that allows you to access the download area.
    - **Password:** The password you'll need to access the files.
    - **Expiration Date:** The date until your subscription is valid.

2. **Access the Download Page:** Open your web browser and navigate to the
   following URL:

    ```txt
    https://cloud.3mdeb.com/index.php/s/{download_key}
    ```

    Replace `{download_key}` with the download key provided in your email.

3. **Enter Your Password:** Once you visit the above link, you'll be prompted
   to enter a password. Use the password from your subscription email.

4. **Download the Binaries:** After entering the password, you can access the
   cloud folder containing the binaries. You can now download them as needed.

**Example:**

- Suppose your download key is `abc123` and your password is
  `securepassword123`.
- You can visit `https://cloud.3mdeb.com/index.php/s/abc123`.
- When prompted, you would enter `securepassword123` as the password.
- After authentication, you can download your subscribed binaries.

**Notes:**

- Ensure you enter the download key and password exactly as they appear in your
  email, as they are case-sensitive.
- If you have not received your email or cannot find it, check your spam folder
  or contact Dasharo support for assistance.

Following these steps, you can access and download your Dasharo Pro Package
binaries without issues. If you encounter any problems, don't
hesitate to contact the Dasharo support team for further assistance.

## Does the Pro Package keys have any bearing on the hardware or BIOS?

The keys/credentials are used by the Dasharo Tools Suite only (a compact
Linux distributions developed for the purpose of simplifying Dasharo
firmware deployment and updates) to:

- determine your subscription type (heads or UEFI flavor of the firmware),
- determine your subscription validity (whether the subscription is
valid for the platform you try to install Dasharo on),
- download the firmware binaries to install or update Dasharo for the
platform (binaries are not unique, Dasharo Tools Suite downloads the
same binaries for every subscriber for given platform and subscription
type),
- locate HCL report for your specific platform, that was made
during initial deployment of Dasharo firmware in a scenario where you
would like to install back the original firmware (HCL reports contains a
dup of the previous firmware and is used to flash it back on the
platform). Not all platform support restoring the original firmware,
i.e. NovaCustom laptops are shipped only with Dasharo firmware and can't
be flashed with proprietary firmware using this method.

The keys/credentials have no other usages outside Dasharo Tools Suite
and have no impact on other components of the system.

## How can I unsubscribe from a DPP newsletter

Emails sent from DPP newsletters have an `Unsubscribe` link at the bottom, which
will take you to Listmonk's unsubscribe form.

If you choose to `Unsubscribe from all future e-mails`, you will be blocklisted
from every list in 3mdeb Listmonk's instance. It is currently impossible to
unsubscribe from only one private list - see [related issue][listmonk-issue].

!!! warning

    Choosing `Wipe your data` will remove you from Listmonk and revoke your DPP
    access. Please refrain from using this option.

[listmonk-issue]: https://github.com/knadh/listmonk/issues/2382

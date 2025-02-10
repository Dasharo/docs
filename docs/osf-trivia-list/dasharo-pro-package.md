# Frequently Asked Questions about Dasharo Pro Package

## How can I download the Dasharo Pro Package binaries?

If you've purchased the Dasharo Pro Package, you should have received an
email containing all the necessary details to access your binaries. Here's how
you can download them:

1. **Locate Your Email:** Check the email account you used to purchase the
   subscription. Look for an email from Dasharo that includes your subscription
   data. This email will contain several vital pieces of information:

    - **Password:** The password you'll need to access the files.
    - **Expiration Date:** The date until your subscription is valid.

2. **Access the Download Page:** Open your web browser and navigate to the
   following URL:

    ```txt
    https://dl.dasharo.com
    ```

3. **Enter Your Password:** Once you visit the above link, you'll be prompted
   to enter a username and password. Use the password from your subscription
   email. The username is your email address.

4. **Download the Binaries:** After entering the password, you can access the
   bucket containing the binaries. You can now download them as needed.

**Notes:**

- Ensure you enter the password exactly as it appears in your email, as it is
  case-sensitive.
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

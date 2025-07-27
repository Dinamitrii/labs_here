options = ChromeOptions()
options.browser_version = "134"
options.platform_name = "Windows 10"
lt_options = {};
lt_options["username"] = "vesterosbg";
lt_options["accessKey"] = "LT_jCeNq7eIWIlmuMPqW5ovQRpOPsqBKF9ZMXiXMTdxqim7gfZ";
lt_options["geoLocation"] = "BG";
lt_options["resolution"] = "1920x1200";
lt_options["timezone"] = "Sofia";
lt_options["project"] = "Untitled";
lt_options["name"] = "tester";
lt_options["tags"] = ["tester"];
lt_options["console"] = "info";
lt_options["w3c"] = True;
lt_options["plugin"] = "python-python";
options.set_capability('LT:Options', lt_options);
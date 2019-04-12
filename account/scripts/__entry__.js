// Contains links for app: account
(context => {
    DMP_CONTEXT.loadBundle({
        "account/index": function() {
            require("./index.js");
            require("./../styles/index.css");
        },
        "account/sign-up": function() {
        },
        "account/base_ajax": function() {
        },
        "account/app_base": function() {
        },
    });
})(DMP_CONTEXT.get());
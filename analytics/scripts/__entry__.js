// Contains links for app: analytics
(context => {
    DMP_CONTEXT.loadBundle({
        "analytics/index": function() {
            require("./index.js");
            require("./../styles/index.css");
        },
        "analytics/base_ajax": function() {
        },
        "analytics/app_base": function() {
        },
    });
})(DMP_CONTEXT.get());
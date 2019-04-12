// Contains links for app: dashboard
(context => {
    DMP_CONTEXT.loadBundle({
        "dashboard/index": function() {
            require("./index.js");
            require("./../styles/index.css");
        },
        "dashboard/base_ajax": function() {
        },
        "dashboard/app_base": function() {
        },
    });
})(DMP_CONTEXT.get());
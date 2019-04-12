// Contains links for app: prescribers
(context => {
    DMP_CONTEXT.loadBundle({
        "prescribers/index": function() {
            require("./index.js");
            require("./../styles/index.css");
        },
        "prescribers/base_ajax": function() {
        },
        "prescribers/app_base": function() {
        },
    });
})(DMP_CONTEXT.get());
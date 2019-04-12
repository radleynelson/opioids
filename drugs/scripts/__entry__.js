// Contains links for app: drugs
(context => {
    DMP_CONTEXT.loadBundle({
        "drugs/index": function() {
            require("./index.js");
            require("./../styles/index.css");
        },
        "drugs/base_ajax": function() {
        },
        "drugs/app_base": function() {
        },
    });
})(DMP_CONTEXT.get());
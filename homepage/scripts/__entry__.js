// Contains links for app: homepage
(context => {
    DMP_CONTEXT.loadBundle({
        "homepage/index": function() {
            require("./index.js");
            require("./../styles/index.css");
        },
        "homepage/base_ajax": function() {
        },
        "homepage/base": function() {
            require("./../styles/base.css");
        },
    });
})(DMP_CONTEXT.get());
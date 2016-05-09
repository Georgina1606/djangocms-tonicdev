window.djangocms_tonicdev_render = function(source, opts, callback) {
    try {
        var notebook = Tonic.createNotebook({
            element: document.getElementById(opts.variable_name + "_element"),
            source: source,
            readOnly: opts.readonly,
            nodeVersion: opts.node_version,
            onURLChanged: function(notebook) {
                console.log("Tonic Notebook {{ instance.ident }} URL:", notebook.URL);
            }
        });
        callback(undefined, notebook);
    } catch(err) {
        console.log(err);
        callback(err);
    }
}
// import EpicEditor doesn't work - the source doesn't explicitly export it :(
import NotReallyAnEpicEditor from 'epiceditor/epiceditor/js/epiceditor.min.js'

document.addEventListener('DOMContentLoaded', function(event) {
    var ids = ['id_summary', 'id_content'];
    var basePath = document.getElementById('article-form').dataset.editorBasePath;
    ids.forEach(function(textareaId) {
        var textarea = document.getElementById(textareaId),
            containerId = 'epic_' + textareaId,
            container = document.createElement('div'),
            label = document.querySelector('label[for="' + textareaId + '"]');
        textarea.style.display = 'none';
        container.id = containerId;
        label.parentNode.appendChild(container);
        var opts = {
            container: containerId,
            textarea: textareaId,
            basePath: basePath,
            clientSideStorage: false,
            button: {
                preview: false
            }
        };
        var editor = new EpicEditor(opts).load();
    });
});

// for some weird reason EpicEditor exports only the Markdown parser
import marked from 'epiceditor/epiceditor/js/epiceditor.min.js'

document.addEventListener('DOMContentLoaded', e => {
    const ids = ['id_summary', 'id_content']
    const basePath = document.getElementById('article-form').dataset.editorBasePath
    ids.forEach(textareaId => {
        document.getElementById(textareaId).style.display = 'none'
        const containerId = `epic_${textareaId}`
        const label = document.querySelector(`label[for="${textareaId}"]`)
        let container = document.createElement('div')
        container.id = containerId
        label.parentNode.appendChild(container)
        let opts = {
            container: containerId,
            textarea: textareaId,
            basePath: basePath,
            clientSideStorage: false,
            parser: marked,
            button: {
                preview: false
            }
        }
        new EpicEditor(opts).load()
    })
})

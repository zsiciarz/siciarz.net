import $ from 'jquery'
import bootstrap from 'bootstrap'
import Pjax from 'pjax'


new Pjax({
  elements: '.pjaxer',
  selectors: ['#base-content']
})

define(['jquery'],function($){$(document).ready(function(){var nifValue=$('input#vat_id').val();if(nifValue==''){$('input#company').val('');$('input#soy_emp').prop('checked',false);$('.field.company').hide();$('.field.taxvat').hide();$('.company_message').hide();}else{$('input#soy_emp').prop('checked',true);}});$('input#soy_emp').click(function(){if($(this).is(':checked')){$('.field.company').show();$('.field.taxvat').show();$('.company_message').show();}else{$('.field.company').hide();$('.field.taxvat').hide();$('input#company').val('');$('input#vat_id').val('');$('.company_message').hide();$('#comp_error').addClass('hidden');}});});
import { call, configureForm, configureNamespace, notify } from "../base.js";

function autofillForm() {
  $("#custom-router_id").val(36);
  $("#custom-ip_address").val("192.168.155.1");
  $("#custom-carry_customer_traffic").prop("checked", true);
  notify("Values filled programatically in JavaScript.", "success", 5);
}

function resetForm() {
  $("[id^='custom-']").val("").prop("checked", false);
  notify("Values resetted programatically in JavaScript.", "success", 5);
}

function submitForm() {
  call({
    url: "/process_form_data",
    form: "custom-form",
    callback: function(result) {
      console.log(result)
      notify("Form response.", "success", 5, true);
    },
  });
}

$(document).ready(function() {
  configureForm("custom");
});

configureNamespace("custom", [autofillForm, resetForm, submitForm]);
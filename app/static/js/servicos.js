$(document).ready(function(){
  $('.update-btn').on('click', (e) => {
    let atendId = $(e.target).attr('atend_id');
    if ($(e.target).parents(".servico-card-pendente").length == 1) {
      console.log("servico pendente");
      $("#confirm").on('click', () => {
        staffCode = $('#staff-code').val();
        if (staffCode) {
          console.log(staffCode, atendId);
          req = $.ajax({
            url: '/process-atendimento',
            type: 'POST',
            data: { id: atendId, code: staffCode }
          });
        }
      });
    } else {
      req = $.ajax({
        url: '/process-atendimento',
        type: 'POST',
        data: { id : atendId, code: '' }
      })
    }
    // let atendElem = $("#servico-card-" + atendId).detach();
    // console.log(`movendo ${'servico-card' + atendId}`);
  })
});

$(document).ajaxComplete(() => {
  location.reload();
});
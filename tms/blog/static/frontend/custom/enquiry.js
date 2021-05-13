$(document).ready(function () {
    function getEnquiry() {
        $.ajax({
            type: 'GET',
            url: 'http://127.0.0.1:8000/enquiry-get',
            success: function (response) {
                var data = response.enquiryData;
                showEnquiry(data);
            }
        })

    }

    getEnquiry();

    function showEnquiry(empData) {
        var outPut = ""
        empData.forEach((emp, key) => {
            outPut += `<tr>`;
            outPut += `<td>${++key}</td>`;
            outPut += `<td>${emp.full_name}</td>`;
            outPut += `<td>${emp.email}</td>`;
            outPut += `<td>${emp.subject}</td>`;
            outPut += `<td>${emp.details}</td>`;
            outPut += `<td>
                        <button class="editEnquiry" data-id="${emp.id}">Edit</button>
                        <button class="deleteEnquiry" data-id="${emp.id}">Delete</button>
                    </td>`;
            outPut += '</tr>'
        });

        $('#enquiryList').html(outPut);

        $('.deleteEnquiry').each((i, items) => {
            $(items).click(function () {
                deleteRecord(items)
            });
        })
        $('.editEnquiry').each((i, items) => {
            $(items).click(function () {
                getByCriteria(items)
            });
        });
    }

    $('#addEnquiry').click(function (e) {
        e.preventDefault();
        var criteria = $('#criteria').val();
        if (criteria == '') {
            var full_name = $('#full_name').val();
            var email = $('#email').val();
            var subject = $('#subject').val();
            var details = $('#details').val();
            var send_data = {
                full_name: full_name,
                email: email,
                subject: subject,
                details: details
            }
            insertEnquiry(send_data);
        } else {
            var full_name = $('#full_name').val();
            var email = $('#email').val();
            var subject = $('#subject').val();
            var details = $('#details').val();
            var send_data = {
                full_name: full_name,
                email: email,
                subject: subject,
                details: details
            }
            updateEnquiry(criteria, send_data);
        }

    });

    function insertEnquiry(data) {
        const csrftoken = document.querySelector('[name=csrfmiddlewaretoken]').value;
        var sendUrl = 'http://127.0.0.1:8000/enquiry-insert'
        $.ajax({
            type: "POST",
            url: sendUrl,
            data: data,
            headers: {'X-CSRFToken': csrftoken},
            success: function (response) {
                var message = response.success;
                Swal.fire({
                    icon: 'success',
                    title: 'inserted ....',
                    text: message,
                    timer: 2000
                });
                $('#myForm')[0].reset();
                getEnquiry();
            }
        })
    }


    function deleteRecord(criteria) {
        var id = $(criteria).data('id');
        var sendUrl = 'http://127.0.0.1:8000/enquiry-delete/' + id
        $.ajax({
            type: "GET",
            url: sendUrl,
            success: function (response) {
                var message = response.success;
                Swal.fire({
                    icon: 'success',
                    title: 'deleted ....',
                    text: message,
                    timer: 2000
                });
                getEnquiry();
            }
        });
    }

    function getByCriteria(criteria) {
        var id = $(criteria).data('id');
        var sendUrl = 'http://127.0.0.1:8000/enquiry-edit/' + id
        $.ajax({
            type: "GET",
            url: sendUrl,
            success: function (response) {
                $('#criteria').val(response.id);
                var full_name = $('#full_name').val(response.full_name);
                var email = $('#email').val(response.email);
                var subject = $('#subject').val(response.subject);
                var details = $('#details').val(response.details);
                getEnquiry();
            }
        });
    }

    function updateEnquiry(id, data) {
        const csrftoken = document.querySelector('[name=csrfmiddlewaretoken]').value;
        var sendUrl = 'http://127.0.0.1:8000/enquiry-update/' + id;
        $.ajax({
            type: "POST",
            url: sendUrl,
            data: data,
            headers: {'X-CSRFToken': csrftoken},
            success: function (response) {
                var message = response.success;
                Swal.fire({
                    icon: 'success',
                    title: 'inserted ....',
                    text: message,
                    timer: 2000
                });
                $('#myForm')[0].reset();
                getEnquiry();
            }
        })
    }
});
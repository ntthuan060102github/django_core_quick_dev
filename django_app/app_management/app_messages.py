class MessageManager:
    survey = {
        "create": {
            "SUCCESS": "Tạo khảo sát thành công!",
            "INVALID_INPUT": "Dữ liệu đầu vào không hợp lệ!",
            "INTERNAL_SERVER_ERROR": "Lỗi hệ thống!"
        },
        "retrieve":{
            "OBJECT_NOT_FOUND": "Khảo sát không tồn tại hoặc đã bị xóa bởi tác giả!",
            "INTERNAL_SERVER_ERROR": "Lỗi hệ thống!",
            "not_allowed_to_access": "Bạn không có quyền truy cập khảo sát này!"

        },
        "submit": {
            "SUCCESS": "Hệ thống đã ghi lại câu trả lời của bạn!",
            "INVALID_INPUT": "Lỗi toàn vẹn dữ liệu! Rất tiếc vì sự cố hy hữu này!",
            "INTERNAL_SERVER_ERROR": "Lỗi hệ thống! Câu trả lời của bạn lưu không thành công!",
            "done": "<b>Bạn đã thực hiện khảo sát này rồi!</b></br>Cảm ơn vì sự đóng góp của bạn!",
            "submitted": "Rất tiếc, bạn không thể thực hiện lại khảo sát này!",
            "not_allow_blank": "Câu hỏi bắt buộc không được để trống đáp án!",
            "invalid_response_for_non_free_question": "Lỗi hệ thống! Phản hồi cho câu hỏi không tự do không hợp lệ!",
            "not_enough_responses": "Lỗi hệ thống! Số lượng phản hồi được gửi đi không đủ!",
            "not_the_same_survey": "Lỗi hệ thống! Các phản hồi không thuộc cùng khảo sát!",
            "not_allow_multiple_choices": "Lỗi hệ thống! Câu hỏi đơn phản hồi không thể chọn (điền) cùng lúc nhiều câu trả lời!",
            "does_not_exist": "Lỗi hệ thống! Không tìm thấy đầy đủ thông tin trong phản hồi của bạn!"
        }
    }

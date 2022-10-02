class CreatePostPageConsts:
    TITLE_FIELD_XPATH = ".//input[@id='post-title']"
    BODY_FIELD_XPATH = ".//textarea[@id='post-body']"
    CREATE_POST_BUTTON_XPATH = ".//button[@class='btn btn-primary']"
    SUCCESS_MESSAGE_XPATH = ".//div[@class='alert alert-success text-center']"
    SUCCESS_MESSAGE_TEXT = "New post successfully created."
<<<<<<< HEAD
    DELETE_POST_XPATH = ".//button[@class= 'delete-post-button text-danger']"
    SUCCESS_DELETE_MESSAGE_XPATH = ".//div[@class = 'alert alert-success text-center']"
    SUCCESS_DELETE_MESSAGE_TEXT = "Post successfully deleted"
=======
>>>>>>> origin/homework
    EDIT_POST_BUTTON_XPATH = ".//a[@class='text-primary mr-2']"
    EDIT_MESSAGE_XPATH = ".//div[contains(text(),'Post successfully updated.')]"
    EDIT_MESSAGE_TEXT = "Post successfully updated."
    UPDATE_POST_BUTTON_XPATH = ".//button[contains(text(),'Save Updates')]"
<<<<<<< HEAD
    UPDATE_POST_TITLE_TEXT = "New title"
    UPDATE_POST_BODY_TEXT = "New message"
    CHECKBOX_XPATH = ".//input[@type='checkbox']"
    POST_SELECT_XPATH = ".//select[@id='select1']"
    POST_SELECT_PRIVATE_TEXT = "One Person"
    POST_SELECT_PRIVATE_XPATH = f".//u[contains(text(),'{POST_SELECT_PRIVATE_TEXT}')]"
    POST_SELECT_ALL_USERS_XPATH = f".//u[contains(text(), 'All Users')]"
    POST_SELECT_ALL_USERS_TEXT = "All Users"
    POST_SELECT_GROUP_MESSAGE_XPATH = ".//u[contains(text(), 'Group Message')]"
    POST_SELECT_GROUP_MESSAGE_TEXT = "Group Message"
=======
    UPDATE_POST_TITLE_TEXT = "Title is updated"
    UPDATE_POST_BODY_TEXT = "Body content is updated"
    DELETE_POST_BUTTON_XPATH = ".//button[@class='delete-post-button text-danger']"
    DELETE_MESSAGE_XPATH = ".//div[contains(text(),'Post successfully deleted')]"
    DELETE_MESSAGE_TEXT = "Post successfully deleted"
>>>>>>> origin/homework

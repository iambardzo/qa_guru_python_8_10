from selene import browser, be, have
import resources


class RegistrationPage:
    def open_page(self):
        browser.open('/automation-practice-form')
        return self

    def fill_first_name(self, value):
        browser.element('#firstName').should(be.blank).type(value)
        return self

    def fill_last_name(self, value):
        browser.element('#lastName').should(be.blank).type(value)
        return self

    def fill_email(self, value):
        browser.element('#userEmail').should(be.blank).type('email@example.com')
        return self

    def gender_selection(self, value):
        browser.all('label[for^="gender-radio"]').element_by(have.exact_text(value)).click()
        return self

    def fill_user_number(self, value):
        browser.element('#userNumber').should(be.blank).type(value)
        return self

    def fill_date_of_birth(self, year, month, day):
        browser.element('#dateOfBirthInput').should(be.visible).click()
        browser.element('.react-datepicker__month-select').send_keys(month)
        browser.element('.react-datepicker__year-select').click().send_keys(year).press_enter()
        browser.element(f'.react-datepicker__day--0{day}').click()
        return self

    def select_subject(self, value):
        browser.element('#subjectsInput').type(value)
        browser.all('.subjects-auto-complete__option').element_by(have.exact_text('Maths')).click()
        browser.all('.subjects-auto-complete__multi-value__label').should(have.exact_texts('Maths'))
        return self

    def select_hobbies(self, value):
        browser.all('label[for^="hobbies-checkbox"]').element_by(have.exact_text(value)).click()
        return self

    def add_file(self, file_name):
        browser.element('#uploadPicture').send_keys(resources.path(file_name))
        return self

    def fill_current_adress(self, value):
        browser.element('#currentAddress').type(value)
        return self

    def select_state(self, value):
        browser.element('#react-select-3-input').type(value).press_enter()
        return self

    def select_city(self, value):
        browser.element('#react-select-4-input').type(value).press_enter()
        return self

    def submit_form(self):
        browser.element('#react-select-4-input').press_enter()
        return self

    def registered_user_with(self, first_and_last_name, email, gender, number, date_of_birth,
                             subjects, hobbies, file, current_address, state_and_city):
        browser.element('.table').all('td').even.should(
            have.exact_texts(
                first_and_last_name,
                email,
                gender,
                number,
                date_of_birth,
                subjects,
                hobbies,
                file,
                current_address,
                state_and_city
            )
        )
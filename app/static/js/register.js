document.addEventListener("DOMContentLoaded", () => {
    const form = document.getElementById("register-form");
    const submitBtn = document.getElementById("register-form-submit");
    const inputs = Array.from(form.querySelectorAll('input[required]'));

    function checkInputs() {
        const allValid = inputs.every(input => {
            if (input.type === 'checkbox') return input.checked;
            if (input.type === 'radio') {
                const group = form.querySelectorAll(`input[name="${CSS.escape(input.name)}"]`);
                return Array.from(group).some(r => r.checked);
            }
            return input.value.trim() !== '';
        });

        const constraintOK = form.checkValidity();

        submitBtn.disabled = !(allValid && constraintOK);
        return !submitBtn.disabled;
    }

    inputs.forEach(input => {
        const ev = (input.type === 'checkbox' || input.type === 'radio') ? 'change' : 'input';
        input.addEventListener(ev, checkInputs);
    });

    checkInputs();


    form.addEventListener('submit', async function(e) {
        e.preventDefault();

        inputs.forEach(i => i.style.borderColor = 'var(--accent-color)');

        let valid = true;

        inputs.forEach(input => {
            if (input.type === 'checkbox') {
                if (!input.checked) {
                    valid = false;
                    input.style.borderColor = 'red';
                }
            } else if (input.type === 'radio') {
                const group = form.querySelectorAll(`input[name="${CSS.escape(input.name)}"]`);
                if (!Array.from(group).some(r => r.checked)) {
                    valid = false;
                    group[0].style.outline = '1px solid red';
                }
            } else {
                if (!input.value.trim()) {
                    valid = false;
                    input.style.borderColor = 'red';
                }
            }
            });

            const pswd = form.querySelector('#password');
            const pswd_confirm = form.querySelector('#confirm-password');
            if (pswd && pswd_confirm && pswd.value !== pswd_confirm.value) {
                valid = false;
                pswd.style.borderColor = 'red';
                pswd_confirm.style.borderColor = 'red';
            }

            if (valid) {
                const formData = new FormData(form);
                const response = await fetch('/register', {
                    method: 'POST',
                    body: formData,
                });
            }
        });
    });
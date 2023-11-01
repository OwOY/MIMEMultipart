## How to use Mako
<br>

1. install package
    ```
    python -m pip install mako
    ```
2. create template file  
    [email_template.html](email_template.html)

3. render body
    ```
    from mako.template import Template


    body = Template(filename='email_template.html').render(
        FCTID='FCTID',
        upload_status=True,
        cols=cols,
        data_list=data_list
        error_msg='test'
    )
    ```
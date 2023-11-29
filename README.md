## Awwsistant Python

    cp .env.example .env
    make test

## Examples of OpenAI functions

Run `make test` to get the following output:

---
    aww.chat('give me a details for this iban: DE89370400440532013000 and for GB29NWBK60161331926819')

```
    
test.py::test_assistant 
-------------------------------------------------------------------------------- live log call ---------------------------------------------------------------------------------
INFO     awwsistant:awwsistant.py:62 Run status: in_progress
INFO     awwsistant:awwsistant.py:62 Run status: in_progress
INFO     awwsistant:awwsistant.py:62 Run status: in_progress
INFO     root:awwsistant.py:26 Assistant requested get_iban_info({'iban': 'DE89370400440532013000'})
INFO     root:awwsistant.py:26 Assistant requested get_iban_info({'iban': 'GB29NWBK60161331926819'})
INFO     awwsistant:awwsistant.py:62 Run status: requires_action
INFO     awwsistant:awwsistant.py:62 Run status: in_progress
INFO     awwsistant:awwsistant.py:62 Run status: in_progress
INFO     awwsistant:awwsistant.py:62 Run status: in_progress
INFO     awwsistant:awwsistant.py:62 Run status: completed
WARNING  awwsistant:awwsistant.py:68 message: give me a details for this iban: DE89370400440532013000 and for GB29NWBK60161331926819
WARNING  awwsistant:awwsistant.py:68 message: Here are the details for the requested IBANs:

1. IBAN: DE89370400440532013000
   - Bank Name: Commerzbank
   - Account Number: 0532013000
   - Bank Code: 37040044
   - Country: DE (Germany)
   - Checksum: 89
   - Valid: Yes
   - BBAN: 370400440532013000

2. IBAN: GB29NWBK60161331926819
   - Bank Name: NATIONAL WESTMINSTER BANK PUBLIC LIMITED COMPANY
   - Account Number: 31926819
   - Bank Code: NWBK
   - Country: GB (United Kingdom)
   - Checksum: 29
   - Valid: Yes
   - BBAN: NWBK60161331926819
PASSED                                                                                                                                                                   [100%]

             
```

---
    aww.chat('write me a random quote about money.')

```
test.py::test_assistant 
-------------------------------------------------------------------------------- live log call ---------------------------------------------------------------------------------
INFO     awwsistant:awwsistant.py:62 Run status: in_progress
INFO     root:awwsistant.py:26 Assistant requested get_quote({'category': 'money'})
INFO     awwsistant:awwsistant.py:62 Run status: requires_action
INFO     awwsistant:awwsistant.py:62 Run status: completed
WARNING  awwsistant:awwsistant.py:68 message: write me a random quote about money.
WARNING  awwsistant:awwsistant.py:68 message: Here's a random quote about money: "I really don't like talking about money. All I can say is that the Good Lord must have wanted me to have it." - Larry Bird
PASSED             
```
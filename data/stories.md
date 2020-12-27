## happy path
* greet
  - utter_greet
  - info_form
  - form{"name": "info_form"}
  - slot{"requested_slot":"name"}
* inform_name{"name":"Reda El Marhouch"}
  - info_form
  - slot{"name":"Reda El Marhouch"}
  - slot{"requested_slot":"puissance"}
* inform_puissance{"puissance":"16"}
  - info_form
  - slot{"puissance":"16"}
  - slot{"requested_slot":"carburant"}
* inform_carburant{"carburant":"Essence"}
  - info_form
  - slot{"carburant":"Essence"}
  - slot{"requested_slot":"genre"}
* inform_genre{"genre":"homme"}
  - info_form
  - slot{"genre":"homme"}
  - utter_submit
  - form{"name": null}

## New Story

* greet
    - utter_greet
    - info_form
    - form{"name":"info_form"}
    - slot{"requested_slot":"name"}
* inform_name{"name":"anonyme"}
    - slot{"name":"anonyme"}
    - info_form
    - slot{"name":"anonyme"}
    - slot{"requested_slot":"puissance"}
* inform_puissance{"puissance":"23"}
    - slot{"puissance":"23"}
    - info_form
    - slot{"puissance":null}
    - slot{"requested_slot":"puissance"}
* inform_puissance{"puissance":"12"}
    - slot{"puissance":"12"}
    - info_form
    - slot{"puissance":"12"}
    - slot{"requested_slot":"carburant"}
* greet
    - info_form
    - slot{"carburant":null}
    - slot{"requested_slot":"carburant"}
* inform_carburant{"carburant":"Essence"}
    - slot{"carburant":"Essence"}
    - info_form
    - slot{"carburant":"Essence"}
    - slot{"requested_slot":"genre"}
* greet
    - info_form
    - slot{"genre":null}
    - slot{"requested_slot":"genre"}
* inform_genre{"genre":"homme"}
    - slot{"genre":"homme"}
    - info_form
    - slot{"genre":"homme"}
    - form{"name":null}
    - slot{"requested_slot":null}

## New Story
* greet
    - utter_greet
    - info_form
    - form{"name":"info_form"}
    - slot{"requested_slot":"name"}
* inform_name{"name":"Tarik Bakkali"}
    - slot{"name":"Tarik Bakkali"}
    - info_form
    - slot{"name":"Tarik Bakkali"}
    - slot{"requested_slot":"puissance"}
* inform_puissance{"puissance":"677"}
    - slot{"puissance":"677"}
    - info_form
    - slot{"puissance":null}
    - slot{"requested_slot":"puissance"}
* inform_puissance{"puissance":"7"}
    - slot{"puissance":"7"}
    - info_form
    - slot{"puissance":"7"}
    - slot{"requested_slot":"carburant"}
* inform_carburant{"carburant":"Diesel"}
    - slot{"carburant":"Diesel"}
    - info_form
    - slot{"carburant":"Diesel"}
    - slot{"requested_slot":"genre"}
* inform_genre{"genre":"homme"}
    - slot{"genre":"homme"}
    - info_form
    - slot{"genre":"homme"}
    - form{"name":null}
    - slot{"requested_slot":null}

import { useState } from "react";
import { useForm } from "react-hook-form";

import createEventImage from "@shared/assets/images/piggyBank.png";

import { InputForm } from "@shared/ui/inputForm";
import { Button } from "@shared/ui/button";
import { Checkbox } from "@shared/ui/checkbox";

import { PopUp } from "@shared/ui/popUp";

import "./createGoal.scss";

export function CreateGoal(props) {
  const { isActive = true } = props;
  const [popUpActive, setPopUpActive] = useState(isActive);

  const {
    register,
    handleSubmit,
    formState: { errors, isValid },
  } = useForm({
    defaultValues: {
      name: "",
      group: 0,
      is_active: true,
      final_value: "",
    },
    mode: "onChange",
  });

  const onSubmit = (values) => {
    setPopUpActive(false);
    console.log(values);
  };

  return (
    <PopUp active={popUpActive}>
      <form onSubmit={handleSubmit(onSubmit)} className="create-event-form">
        <div className="create-event-form__header">
          <img
            className="create-event-form__image"
            src={createEventImage}
            alt="Piggy Bank"
          />
          <div className="create-event-form__header1"></div>
        </div>

        <InputForm
          placeholder={"Enter Goal Name"}
          className={"create-event-form__input"}
          error={Boolean(errors.name?.message)}
          errorMessage={errors.name?.message}
          properties={{
            ...register("name", {
              required: true,
            }),
          }}
        />
        
        <InputForm
          placeholder={"Enter final value"}
          className={"create-event-form__input"}
          error={Boolean(errors.username?.message)}
          errorMessage={errors.username?.message}
          properties={{
            ...register("final_value", {
              validate: {
                positive: (value) => {
                  if (parseInt(value) <= 0) {
                    return "Final Value cannot be less or equal then 0";
                  }
                },
              },
            }),
          }}
        />

        <Checkbox
          className={"create-event-form__checkbox"}
          properties={{
            ...register("is_active"),
          }}
        >
          Keep the target active?
        </Checkbox>
        <Button className={"create-event-form__sumbit"} type={"submit"}>
          Create Group
        </Button>
      </form>
    </PopUp>
  );
}

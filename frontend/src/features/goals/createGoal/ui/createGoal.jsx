import { useForm } from "react-hook-form";

import createEventImage from "@shared/assets/images/piggyBank.png";

import { createGoal } from "@shared/api/group";
import { InputForm } from "@shared/ui/inputForm";
import { Button } from "@shared/ui/button";
import { Checkbox } from "@shared/ui/checkbox";

import { PopUp } from "@shared/ui/popUp";

import "./createGoal.scss";

export function CreateGoal(props) {
  const { id, popUpActive, tooglePopUp } = props;

  const {
    register,
    handleSubmit,
    formState: { errors, isValid },
    reset,
  } = useForm({
    defaultValues: {
      name: "",
      group: parseInt(id),
      is_active: true,
      final_value: "",
    },
    mode: "onChange",
  });

  const onSubmit = (values) => {
    tooglePopUp();
    createGoal(values);
    reset();
  };

  return (
    <PopUp isOpenPopUp={popUpActive} closePopUp={tooglePopUp}>
      <form onSubmit={handleSubmit(onSubmit)} className="create-goal-form">
        <div className="create-goal-form__header">
          <img
            className="create-goal-form__image"
            src={createEventImage}
            alt="Piggy Bank"
          />
          <div className="create-goal-form__header1"></div>
        </div>

        <InputForm
          placeholder={"Enter Goal Name"}
          className={"create-goal-form__input"}
          error={Boolean(errors.name?.message)}
          errorMessage={errors.name?.message}
          properties={{
            ...register("name", {
              required: true,
            }),
          }}
        />

        <InputForm
          placeholder={"Enter Final Value"}
          className={"create-goal-form__input"}
          error={Boolean(errors.final_value?.message)}
          errorMessage={errors.final_value?.message}
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
          className={"create-goal-form__checkbox"}
          properties={{
            ...register("is_active"),
          }}
        >
          Keep the target active?
        </Checkbox>
        <Button className={"create-goal-form__sumbit"} type={"submit"}>
          Create New Goal
        </Button>
      </form>
    </PopUp>
  );
}

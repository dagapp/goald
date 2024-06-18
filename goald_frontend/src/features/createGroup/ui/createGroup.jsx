import { useForm } from "react-hook-form";

import createGroupImage from "@shared/assets/images/groupFormImage.png";

import { InputForm } from "@shared/ui/inputForm";
import { Button } from "@shared/ui/button";
import { Checkbox } from "@shared/ui/checkbox";

import { PopUp } from "@shared/ui/popUp";

import "./createGroup.scss";

export function CreateGroup(props) {
  const { popUpActive, tooglePopUp } = props;

  const {
    register,
    handleSubmit,
    formState: { errors, isValid },
    reset,
  } = useForm({
    defaultValues: {
      name: "",
      tag: "",
      is_public: true,
      group_image: "",
    },
    mode: "onSubmit",
  });

  const onSubmit = (values) => {
    tooglePopUp();
    console.log(values);
    reset();
  };

  return (
    <PopUp isOpenPopUp={popUpActive} closePopUp={tooglePopUp}>
      <form onSubmit={handleSubmit(onSubmit)} className="create-group-form">
        <div className="create-group-form__header">
          <img
            className="create-group-form__image"
            src={createGroupImage}
            alt="Group Image"
          />
          <div className="create-group-form__header"></div>
        </div>

        <InputForm
          placeholder={"Enter Group Name"}
          className={"create-group-form__input"}
          error={Boolean(errors.name?.message)}
          errorMessage={errors.name?.message}
          properties={{
            ...register("name", {
              required: true,
            }),
          }}
        />

        <InputForm
          placeholder={"Enter Group Tag"}
          className={"create-group-form__input"}
          error={Boolean(errors.tag?.message)}
          errorMessage={errors.tag?.message}
          properties={{
            ...register("tag", {
            }),
          }}
        />

        <Checkbox
          className={"create-group-form__checkbox"}
          properties={{
            ...register("is_public"),
          }}
        >
          Make this Group Public?
        </Checkbox>
        <Button className={"create-group-form__sumbit"} type={"submit"}>
          Create New Group
        </Button>
      </form>
    </PopUp>
  );
}

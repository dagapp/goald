import { useForm } from "react-hook-form";
import { useDispatch } from "react-redux";

import createGroupImage from "@shared/assets/images/groupFormImage.png";
import { createGroup } from "@shared/api/group";
import { InputForm } from "@shared/ui/inputForm";
import { InputFormFile } from "@shared/ui/inputFormFile";
import { Button } from "@shared/ui/button";
import { Checkbox } from "@shared/ui/checkbox";

import { fetchGroupList } from "@features/groupList";
import { PopUp } from "@shared/ui/popUp";

import "./createGroup.scss";
import { useState } from "react";

export function CreateGroup(props) {
  const { popUpActive, tooglePopUp } = props;
  const { loadedImage, isLoadedImage } = useState(false);

  const {
    register,
    handleSubmit,
    formState: { errors, isValid },
    setValue,
    reset,
  } = useForm({
    defaultValues: {
      name: "",
      tag: "",
      is_public: true,
      group_image: "noImage",
    },
    mode: "onSubmit",
  });

  const dispatch = useDispatch();

  const onChangeImage = (event) => {
    console.log(getBase64(event.target.files[0]));
    setValue("group_image", getBase64(event.target.files[0]));
  };

  const onSubmit = (values) => {
    tooglePopUp();
    createGroup(values);
    reset();
    dispatch(fetchGroupList());
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
              required: "Group name should be provided",
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
              required: "Tag should be provided",
            }),
          }}
        />

        <InputFormFile
          placeHolder={"Load your Group Image"}
          //onChange={onChangeImage}
          error={Boolean(errors.tag?.message)}
          errorMessage={errors.tag?.message}
          // properties={{
          //   ...register("group_image", {
          //     required: "Group avatar is required",
          //   }),
          // }}
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

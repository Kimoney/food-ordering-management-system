import React from "react";

function Listing() {
  return (
    <div className="w-[450px] h-[801px] p-2.5 bg-white justify-start items-end gap-[145px] inline-flex">
      <div className="text-orange-600 text-4xl font-bold font-['Montserrat']">
        Hamburger
      </div>
      <img
        className="w-[424.80px] h-[424.28px]"
        src="https://via.placeholder.com/425x424"
        alt="Hamburger"
      />
      <div className="w-[442px] flex-col justify-start items-start gap-5 inline-flex">
        <div className="w-[479.74px] text-black text-2xl font-bold font-['Montserrat']">
          Description
        </div>
        <div className="w-[442px] text-black text-opacity-50 text-base font-normal font-['Montserrat']">
          "Sink your teeth into our classic hamburger, crafted with 100% beef
          patty, fresh lettuce, ripe tomatoes, and our secret sauce, all nestled
          between soft, toasted buns. It's a taste sensation you won't forget!"
        </div>
      </div>
      <div className="w-[198px] text-black text-base font-extrabold font-['Inter']">
        Ksh.450
      </div>
      <div className="justify-center items-center gap-3 flex">
        <div className="w-[28.21px] text-black text-base font-normal font-['Inter']">
          1
        </div>
      </div>
      <div className="p-2.5 bg-orange-600 rounded-[10px] justify-center items-center gap-2.5 flex">
        <div className="text-white text-base font-normal font-['Inter']">
          Add to Cart
        </div>
      </div>
    </div>
  );
}

export default Listing;

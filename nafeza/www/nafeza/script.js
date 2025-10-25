// ✅ عناصر DOM
const sidebar = document.getElementById("sidebar");
const openBtn = document.querySelector(".open-sidebar-tasks-btn");
const closeBtn = document.querySelector(".sidebar .close-btn");

const sidebarMain = document.getElementById("sidebar-main");
const sidebarAttachments = document.getElementById("sidebar-attachments");

const attachmentsBtn = document.getElementById("attachmentsBtn");
const backBtn = document.getElementById("backBtn");

const containerFluid = document.querySelector(".container-fluid");
const containerImgBox = document.querySelector(".containerimg");

// ✅ فتح القائمة الجانبية
openBtn.addEventListener("click", () => {
  sidebar.classList.add("active");
});

// ✅ إغلاق القائمة الجانبية
closeBtn.addEventListener("click", () => {
  sidebar.classList.remove("active");
});

// ✅ عند الضغط على "صور المرفقات"
attachmentsBtn.addEventListener("click", () => {
  sidebarMain.style.display = "none";
  sidebarAttachments.style.display = "block";
  containerFluid.style.display = "none";  // إخفاء البيانات الأساسية
  containerImgBox.style.display = "block"; // إظهار الصور
});

// ✅ عند الضغط على "عودة"
backBtn.addEventListener("click", () => {
  sidebarAttachments.style.display = "none";
  sidebarMain.style.display = "block";
  containerFluid.style.display = "block"; // إظهار البيانات الأساسية
  containerImgBox.style.display = "none"; // إخفاء الصور
});

// ✅ جدول المرفقات (اختيار صورة عند الضغط على الصف)
const tableRows = document.querySelectorAll(".attachments-table tbody tr");
const imgList = document.querySelector(".img-list");

// صور تجريبية مرتبطة بالوصف
const attachmentsImages = {
  "فاتورة مبدئية": "https://picsum.photos/id/1015/1200/800",
  "شهادة منشأ": "https://picsum.photos/id/1025/1200/800",
  "بوليصة شحن": "https://picsum.photos/id/1035/1200/800"
};

// عند الضغط على صف → تحديث الصورة
tableRows.forEach(row => {
  row.addEventListener("click", () => {
    const desc = row.querySelector("td").textContent.trim();

    imgList.innerHTML = ""; // تفريغ الصور القديمة

    if (attachmentsImages[desc]) {
      const imgBox = document.createElement("div");
      imgBox.classList.add("img-box");

      const img = document.createElement("img");
      img.src = attachmentsImages[desc];
      img.alt = desc;

      imgBox.appendChild(img);
      imgList.appendChild(imgBox);
    } else {
      imgList.innerHTML = `<p style="text-align:center; color:gray;">⚠ لا توجد صورة لهذا المرفق</p>`;
    }
  });
});

// ✅ في البداية: إخفاء الصور
containerImgBox.style.display = "none";
sidebarAttachments.style.display = "none";

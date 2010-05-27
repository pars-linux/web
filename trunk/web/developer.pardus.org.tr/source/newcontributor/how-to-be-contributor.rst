.. _how-to-be-contributor:

How to be a Contributor?
========================

******************************
Applicant Tracking on Bugzilla
******************************

- "Yeni Katkıcı / New Contributor" product is for this tracking process.
- The compoenents of this product are "Geliştirici / Developer" and "Testçi / Tester".
- The translator applications can be held from `Pardus translation website <http://translate.pardus.org.tr>`_.
- The bugzilla permissions:
    - A mentoring group is created for product "Yeni Katkıcı / New Contributor"
    - The users out of the mentoring group can create contributor bugs, but can not edit bugs.

    ..  image:: images/application_process.png

****************
Tracking Process
****************

Application Request
-------------------
#. The applicant creates a `bugzilla <bugs.pardus.org.tr>`_ account if he/she has not yet.
#. The applicant reports a bug for the related component of "Yeni Katkıcı / New Contributor" product.
#. The summary of the bug likes "Testçi veya Geliştirici Adaylık Ad Soyad" "Tester veya Developer Applicant Name Surname".
#. The bug details part should contains the answers of the following personal questions.

    #. What are the distributions that you use properly?
    #. From when and at what level do you use Pardus?
    #. What does it mean for you to contribute to a free software project
    #. Have you ever contributed any free software project before? If yes, which project, in what way, how long?
    #. Why would you want to contribute Pardus?
    #. How much time could you spend for Pardus?
    #. Please attach your short background as an attachment or give links.
    #. If the application is for development, the applicant should also attach these informations that you have already done:
        #. The prepared packages for Pardus repositories, or a improvement for Pardus projects.
        #. The bugs that you have fixed at bugs.pardus.org.tr.
        #. The other contributions that you have done for other distributions.

#. If the application has missing parts or the applicant report his/her bug carelessly, it will be closed with status RESOLVED/INVALID by mentoring coordinators and the `Rejection Stock Response`_ is given.
#. If the applicant gets a rejection at that stage, in the case of his/her effort to Pardus, he/she can reapply in 3 months to be tester, 6 months to be developer.

Sending Quiz to Applicant
-------------------------
#. The mentoring coordinators send quiz as an attachment with `Quiz Sending Stock Response`_.
#. The applicant sends an approval, that he/she starts the quiz.
#. After 10 days of the approval, the applicant commits his/her answers as an attachment to the bug.
#. If the applicant is not responsive in these 10 days, his/her bug will be closed with status RESOLVED/INVALID by mentoring coordinators and the `Rejection Stock Response`_ is given.
#. If the applicant is responsive and has send the answers in 10 days, the answers will be reviewed by mentors and review comments will be given on bugzilla.
#. If the quiz review is negative, his/her bug will be closed with status RESOLVED/INVALID by mentoring coordinators and the `Rejection Stock Response`_ is given.
#. If the applicant gets a rejection at that stage, in the case of his/her effort to Pardus, he/she can reapply in 3 months to be tester, 6 months to be developer.
#. If the quiz review is positive:
    #. If the applicant is applied as a tester, the test team membership will be accepted and tester list permissions will be gived. The acceptence anouncement will be done by mentor coordinators as a `Tester Acceptence Stock Response`_ comment to the bug and the bug status will be changed to RESOLVED/FIXED. 
    #. If the applicant is applied as a developer, a mentor is assigned to him/her.


Assigning Mentor
----------------
#. A mentor is assigned related to applicant responses.
    #. One mentor has maximum 3 applicants
    #. If all mentors has 3 applicants, the newest applicant should have to wait in the queue. It will be announced by mentoring coordinators with a `Waiting in the Queue Stock Response`_ comment.
    #. The mentor coordinators will be tracked:
        #. The number of applicant on mentor.
        #. Send ping mails to mentor@pardus.org.tr in order to assign mentor to an applicant.
    #. When a mentor is assigned to an applicant, the mentoring coordinators send `Assigning Mentor Stock Response`_ as a comment to the bug. The coordinator will also change the keyword as "MENTOR" and reassign the bug to related applicant mentor.

Mentoring Process
-----------------
#. The mentor will give applicant some junior jobs. (The junior job can be a bug or package.)
    #. Related to junior jobs difficulty, one more jobs can be given to applicant.
    #. At this stage playground svn permissions will be given to applicant. (The mentor will send and an email to sys. Admin for giving permissions.)
    #. For giving svn permissions, mentor send a `Creating SVN Account Stock Response`_ comment to bugzilla and the applicant should send the needed information as a bug comment.
    #. The owner of the packages that applicant has done will be his/her mentor.
#. If the applicant might not have achieved to finish the applicant job until the deadline, his/her bug will be closed with status RESOLVED/INVALID by the mentor and related comment will be given. Mentor can also add the reapply time to the comment. (Reapply time is depended to mentor related to applicant performance)(The mentor will send and an email to sys. Admin for removing permissions.)
#. If applicant has finished his/her jobs in time:
    #. The applicant is enters applicant progress observation period.

Applicant Progress Observation
------------------------------
#. The applicant process finishing time is related to the his/her mentor.
#. The owner of the packages that applicant has done will be his/her mentor.
#. All svn permissions excluding "stable" will be given to applicant. (The mentor will send and an email to sys. Admin for giving permissions.)
#. Mentor will keep an eye on applicant, until the applicant reach a good level.
    #. He/she joins the package review process of the packages that the applicant done.
    #. He/she controls that the applicant fullfills the `responsibilities of the contributor <http://developer.pardus.org.tr/newcontributor/index.html#responsibilities-of-a-contributor>`_ like continuity, accuracy, determination, communication.
#. If the applicant can not pass this process, his/her bug will be closed with status RESOLVED/INVALID by the mentor and related comment will be given. (The mentor will send and an email to sys. Admin for removing permissions.)
#. If the applicant can pass this process:
    #. When the mentor has been satisfied by applicant, mentor sends a comment as he/she leaves the applicant and changes the bug status as RESOLVED/FIXED
    #. The applicant is called as developer.
    #. All svn permissions will be given to new developer. (The mentor will send and an email to sys. Admin for giving permissions)
    #. All packages and works that the developer has done during his candidacy, are transfered to him/her

Guiding Rules
-------------
#. Until a mentor has been assigned to applicant, the mentor coordinators will track the process. (Traking the applicant bugs, sending quiz, assign mentor etc.)
#. After the mentor has assigned, the mentor is responsible for the applicant. (Tracking his/her applicants, sending necessary comments to bug and editing it etc. )

***************
Stock Responses
***************

Rejection Stock Response
------------------------
    ::

        Başvurunuz olumsuz sonuçlanmıştır. Pardus'a katkı vermeye başladığınız ve kendinizi geliştirdiğiniz takdirde yaklaşık x ay sonra tekrar başvuruda bulunabilirsiniz.
        --
        Pardus Mentor Koordinatörleri

    ::

        Your application is unfavorable. You can reapply again after x months, if you continue to develop your self and start to contribute to Pardus.
        --
        Pardus Mentoring Coordinators

Quiz Sending Stock Response
---------------------------
    ::

       Merhabalar,
       Öncelikle x üyesi başvurunuzu kutlar ve Pardus'a katkıda bulunmak istediğiniz için teşekkür ederiz.
       x ekibi üyeliği sürecinin ilk aşaması olan ve Pardus Linux Dağıtımı alt yapısı ve x süreçleri ile ilgili bilgilendirici nitelikte sorulara sahip olan sınavımızı ekte bulabilirsiniz.

       Kaynaklar,
       x
       y
       z

       Kolay Gelsin,
       --
       Pardus Mentor Koordinatörleri


    ::

       Hi,

       First of all, we want to conragulate your x application and thanks to your desire to contribute to Pardus.
       You can find our informative quiz about Pardus Linux Distribution and x processes as an attachment.

       Resources,

       Regards,
       -- 
       Pardus Mentoring Coordinators

Tester Acceptence Stock Response
--------------------------------

    ::

        Başvurunuz olumlu sonuçlanmıştır,  testçi@pardus.org.tr için gerekli izinleriniz verilmiştir. Pardus'a yapacağınız katkılarda dolayı şimdiden size teşşekür ederiz.
        --
        Pardus Mentor Koordinatörleri
    ::

        Your application is favorable, the permissions about testçi@pardus.org.tr has been given. Thank you in advance for their generous contributions to make for Pardus.
        -- 
        Pardus Mentoring Coordinators

Waiting in the Queue Stock Response
-----------------------------------
    ::

        Şu anda tüm mentor'larımızın slotları doludur, slot'ları uygun olan mentor'lar oluştuğunda size geri dönüş yapılacaktır.
        Bu süre içerisinde Pardus'a yaptığınız katkılara devam edebilir ve kendinizi bu yönde daha fazla geliştirebilir ve mentor sürecinizi kısaltabilirsiniz.

        İyi günler,
        --
        Pardus Mentor Koordinatörleri

    ::

        ll slots of our mentors are occupied, when the slots are available we will back to your application.
        uring this period, you can continue to contribute to Pardus, and may shorten your mentoring process.
        -
        Pardus Mentor Koordinatörleri

Assigning Mentor Stock Response
-------------------------------

    ::

        Göndermiş olduğunuz cevaplar doğrultusunda size x kişisi mentor olarak atanmıştır. 
        http://svn.pardus.org.tr/uludag/trunk/playground/ ve http://svn.pardus.org.tr/pardus/playground/ izinleriniz verilmiştir. Bu aşamada size mentor tarafından küçük iş(ler) verilecektir.

        Bu aşamada yapacağınız çalışmalar için şimdiden kolaylıklar dileriz.
        --
        Pardus Mentor Koordinatörleri
    ::

        Related to your responses, x is assigned you as a mentor. 
        The permissions for http://svn.pardus.org.tr/uludag/trunk/playground/ and http://svn.pardus.org.tr/pardus/playground/ will be given. During this period, your mentor will give you junior jobs.
        Regards,
        -- 
        Pardus Mentoring Coordinators

Creating SVN Account Stock Response
-----------------------------------

    ::

        Merhabalar,

        SVN hesabı açabilmemiz için, aşağıda bulunan bağlantı doğrultusunda elde ettiğiniz çıktıyı bize göndermeniz gerekmektedir

        http://developer.pardus.org.tr/newcontributor/creating-svn-account.html
        Teşekkürler,

    ::

        Hi,

        In order to creating an svn account, you have to send the output that is mentioned below link.

        http://developer.pardus.org.tr/newcontributor/creating-svn-account.html
        Regards,

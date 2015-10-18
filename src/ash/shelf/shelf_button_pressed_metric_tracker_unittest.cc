// Copyright 2015 The Chromium Authors. All rights reserved.
// Use of this source code is governed by a BSD-style license that can be
// found in the LICENSE file.

#include "ash/shelf/shelf_button_pressed_metric_tracker.h"

#include "ash/shelf/shelf.h"
#include "ash/test/ash_test_base.h"
#include "ash/test/shelf_button_pressed_metric_tracker_test_api.h"
#include "ash/test/shelf_test_api.h"
#include "ash/test/shelf_view_test_api.h"
#include "base/macros.h"
#include "base/test/histogram_tester.h"
#include "base/test/simple_test_tick_clock.h"
#include "base/test/user_action_tester.h"
#include "testing/gtest/include/gtest/gtest.h"
#include "ui/events/event.h"
#include "ui/views/controls/button/button.h"

namespace ash {
namespace test {
namespace {

// A simple light weight test double dummy for a views::Button.
class DummyButton : public views::Button {
 public:
  DummyButton();

 private:
  DISALLOW_COPY_AND_ASSIGN(DummyButton);
};

DummyButton::DummyButton() : views::Button(nullptr) {
}

// A simple light weight test double dummy for a ui::Event.
class DummyEvent : public ui::Event {
 public:
  DummyEvent();
  ~DummyEvent() override;
  int unique_id() const { return unique_id_; }

 private:
  static int next_unique_id_;
  int unique_id_;

  DISALLOW_COPY_AND_ASSIGN(DummyEvent);
};

int DummyEvent::next_unique_id_ = 0;

DummyEvent::DummyEvent()
    : Event(ui::ET_GESTURE_TAP, base::TimeDelta(), 0),
      unique_id_(next_unique_id_++) {
}

DummyEvent::~DummyEvent() {
}

// Test fixture for the ShelfButtonPressedMetricTracker class. Relies on
// AshTestBase to initilize the UserMetricsRecorder and it's dependencies.
class ShelfButtonPressedMetricTrackerTest : public AshTestBase {
 public:
  static const char*
      kTimeBetweenWindowMinimizedAndActivatedActionsHistogramName;

  ShelfButtonPressedMetricTrackerTest();
  ~ShelfButtonPressedMetricTrackerTest() override;

  // AshTestBase:
  void SetUp() override;
  void TearDown() override;

  // Calls ButtonPressed on the test target with the given |event|
  // and dummy values for the |sender| and |performed_action| parameters.
  void ButtonPressed(const ui::Event& event);

  // Calls ButtonPressed on the test target with the given |performed_action|
  // and dummy values for the |event| and |sender| parameters.
  void ButtonPressed(ShelfItemDelegate::PerformedAction performed_action);

  // Calls ButtonPressed on the test target with the given |sender| and
  // |performed_action| and a dummy value for the |event| parameter.
  void ButtonPressed(const views::Button* sender,
                     ShelfItemDelegate::PerformedAction performed_action);

 protected:
  // The test target. Not owned.
  ShelfButtonPressedMetricTracker* metric_tracker_;

  // The TickClock injected in to the test target.
  base::SimpleTestTickClock* tick_clock_;

 private:
  DISALLOW_COPY_AND_ASSIGN(ShelfButtonPressedMetricTrackerTest);
};

const char* ShelfButtonPressedMetricTrackerTest::
    kTimeBetweenWindowMinimizedAndActivatedActionsHistogramName =
        ShelfButtonPressedMetricTracker::
            kTimeBetweenWindowMinimizedAndActivatedActionsHistogramName;

ShelfButtonPressedMetricTrackerTest::ShelfButtonPressedMetricTrackerTest() {
}

ShelfButtonPressedMetricTrackerTest::~ShelfButtonPressedMetricTrackerTest() {
}

void ShelfButtonPressedMetricTrackerTest::SetUp() {
  AshTestBase::SetUp();

  Shelf* shelf = Shelf::ForPrimaryDisplay();
  ShelfViewTestAPI shelf_view_test_api(ShelfTestAPI(shelf).shelf_view());

  metric_tracker_ = shelf_view_test_api.shelf_button_pressed_metric_tracker();

  ShelfButtonPressedMetricTrackerTestAPI test_api(metric_tracker_);

  scoped_ptr<base::TickClock> test_tick_clock(new base::SimpleTestTickClock());
  tick_clock_ = static_cast<base::SimpleTestTickClock*>(test_tick_clock.get());
  test_api.SetTickClock(test_tick_clock.Pass());

  // Ensure the TickClock->NowTicks() doesn't return base::TimeTicks because
  // ShelfButtonPressedMetricTracker interprets that value as unset.
  tick_clock_->Advance(base::TimeDelta::FromMilliseconds(100));
}

void ShelfButtonPressedMetricTrackerTest::TearDown() {
  tick_clock_ = nullptr;

  AshTestBase::TearDown();
}

void ShelfButtonPressedMetricTrackerTest::ButtonPressed(
    const ui::Event& event) {
  const DummyButton kDummyButton;
  metric_tracker_->ButtonPressed(event, &kDummyButton,
                                 ShelfItemDelegate::kNoAction);
}

void ShelfButtonPressedMetricTrackerTest::ButtonPressed(
    ShelfItemDelegate::PerformedAction performed_action) {
  const DummyEvent kDummyEvent;
  const DummyButton kDummyButton;
  metric_tracker_->ButtonPressed(kDummyEvent, &kDummyButton, performed_action);
}

void ShelfButtonPressedMetricTrackerTest::ButtonPressed(
    const views::Button* sender,
    ShelfItemDelegate::PerformedAction performed_action) {
  const DummyEvent kDummyEvent;
  metric_tracker_->ButtonPressed(kDummyEvent, sender, performed_action);
}

}  // namespace

// Verifies that a Launcher_ButtonPressed_Mouse UMA user action is recorded when
// a button is pressed by a mouse event.
TEST_F(ShelfButtonPressedMetricTrackerTest,
       Launcher_ButtonPressed_MouseIsRecordedWhenIconActivatedByMouse) {
  const ui::MouseEvent mouse_event(ui::ET_MOUSE_PRESSED, gfx::Point(),
                                   gfx::Point(), base::TimeDelta(), 0, 0);

  base::UserActionTester user_action_tester;
  ButtonPressed(mouse_event);
  EXPECT_EQ(1,
            user_action_tester.GetActionCount("Launcher_ButtonPressed_Mouse"));
}

// Verifies that a Launcher_ButtonPressed_Touch UMA user action is recorded when
// a button is pressed by a touch event.
TEST_F(ShelfButtonPressedMetricTrackerTest,
       Launcher_ButtonPressed_MouseIsRecordedWhenIconActivatedByTouch) {
  const ui::TouchEvent touch_event(ui::ET_GESTURE_TAP, gfx::Point(), 0,
                                   base::TimeDelta());

  base::UserActionTester user_action_tester;
  ButtonPressed(touch_event);
  EXPECT_EQ(1,
            user_action_tester.GetActionCount("Launcher_ButtonPressed_Touch"));
}

// Verifies that a Launcher_LaunchTask UMA user action is recorded when
// pressing a button causes a new window to be created.
TEST_F(ShelfButtonPressedMetricTrackerTest,
       Launcher_LaunchTaskIsRecordedWhenNewWindowIsCreated) {
  base::UserActionTester user_action_tester;
  ButtonPressed(ShelfItemDelegate::kNewWindowCreated);
  EXPECT_EQ(1, user_action_tester.GetActionCount("Launcher_LaunchTask"));
}

// Verifies that a Launcher_MinimizeTask UMA user action is recorded when
// pressing a button causes an existing window to be minimized.
TEST_F(ShelfButtonPressedMetricTrackerTest,
       Launcher_MinimizeTaskIsRecordedWhenWindowIsMinimized) {
  base::UserActionTester user_action_tester;
  ButtonPressed(ShelfItemDelegate::kExistingWindowMinimized);
  EXPECT_EQ(1, user_action_tester.GetActionCount("Launcher_MinimizeTask"));
}

// Verifies that a Launcher_SwitchTask UMA user action is recorded when
// pressing a button causes an existing window to be activated.
TEST_F(ShelfButtonPressedMetricTrackerTest,
       Launcher_SwitchTaskIsRecordedWhenExistingWindowIsActivated) {
  base::UserActionTester user_action_tester;
  ButtonPressed(ShelfItemDelegate::kExistingWindowActivated);
  EXPECT_EQ(1, user_action_tester.GetActionCount("Launcher_SwitchTask"));
}

// Verify that a window activation action will record a data point if it was
// subsequent to a minimize action.
TEST_F(ShelfButtonPressedMetricTrackerTest,
       VerifyDataRecordedAfterMinimizedAndSubsequentActivatedAction) {
  const DummyButton kDummyButton;

  base::HistogramTester histogram_tester;

  ButtonPressed(&kDummyButton, ShelfItemDelegate::kExistingWindowMinimized);
  histogram_tester.ExpectTotalCount(
      kTimeBetweenWindowMinimizedAndActivatedActionsHistogramName, 0);

  ButtonPressed(&kDummyButton, ShelfItemDelegate::kExistingWindowActivated);
  histogram_tester.ExpectTotalCount(
      kTimeBetweenWindowMinimizedAndActivatedActionsHistogramName, 1);
}

// Verify that a multiple window activation actions will record a single data
// point if they are subsequent to a minimize action.
TEST_F(ShelfButtonPressedMetricTrackerTest,
       VerifyDataRecordedAfterMinimizedAndMultipleSubsequentActivatedActions) {
  const DummyButton kDummyButton;

  base::HistogramTester histogram_tester;

  ButtonPressed(&kDummyButton, ShelfItemDelegate::kExistingWindowMinimized);
  ButtonPressed(&kDummyButton, ShelfItemDelegate::kExistingWindowActivated);
  ButtonPressed(&kDummyButton, ShelfItemDelegate::kExistingWindowActivated);

  histogram_tester.ExpectTotalCount(
      kTimeBetweenWindowMinimizedAndActivatedActionsHistogramName, 1);
}

// Verify that a window activation action will not record a data point if it was
// not subsequent to a minimize action.
TEST_F(ShelfButtonPressedMetricTrackerTest,
       VerifyDataRecordedAfterMinimizedAndNonSubsequentActivatedAction) {
  const DummyButton kDummyButton;

  base::HistogramTester histogram_tester;

  ButtonPressed(&kDummyButton, ShelfItemDelegate::kExistingWindowMinimized);
  ButtonPressed(&kDummyButton, ShelfItemDelegate::kAppListMenuShown);
  ButtonPressed(&kDummyButton, ShelfItemDelegate::kExistingWindowActivated);

  histogram_tester.ExpectTotalCount(
      kTimeBetweenWindowMinimizedAndActivatedActionsHistogramName, 0);
}

// Verify no data is recorded if a second source button is pressed in between
// subsequent minimized and activated actions on the same source.
TEST_F(ShelfButtonPressedMetricTrackerTest,
       VerifyDataRecordedAfterMinimizedButtonA) {
  const DummyButton kDummyButton;
  const DummyButton kSecondDummyButton;

  base::HistogramTester histogram_tester;

  ButtonPressed(&kDummyButton, ShelfItemDelegate::kExistingWindowMinimized);
  ButtonPressed(&kSecondDummyButton,
                ShelfItemDelegate::kExistingWindowMinimized);
  ButtonPressed(&kDummyButton, ShelfItemDelegate::kExistingWindowActivated);

  histogram_tester.ExpectTotalCount(
      kTimeBetweenWindowMinimizedAndActivatedActionsHistogramName, 0);
}

// Verify the data value recorded when a window activation action is subsequent
// to a minimize action.
TEST_F(ShelfButtonPressedMetricTrackerTest,
       VerifyTheValueRecordedBySubsequentMinimizedAndActivateActions) {
  const int kTimeDeltaInMilliseconds = 17;
  const DummyButton kDummyButton;

  base::HistogramTester histogram_tester;

  ButtonPressed(&kDummyButton, ShelfItemDelegate::kExistingWindowMinimized);
  tick_clock_->Advance(
      base::TimeDelta::FromMilliseconds(kTimeDeltaInMilliseconds));
  ButtonPressed(&kDummyButton, ShelfItemDelegate::kExistingWindowActivated);

  histogram_tester.ExpectTotalCount(
      kTimeBetweenWindowMinimizedAndActivatedActionsHistogramName, 1);
  histogram_tester.ExpectBucketCount(
      kTimeBetweenWindowMinimizedAndActivatedActionsHistogramName,
      kTimeDeltaInMilliseconds, 1);
}

}  // namespace test
}  // namespace ash
